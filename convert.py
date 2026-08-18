#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NScripter (0.txt) → Ren'Py 转换器
=================================

将《突然之间发现我已恋上你》的 NScripter 脚本转换为 Ren'Py 格式。

用法::

    python3 convert.py [0.txt路径] [游戏目录]

参数说明:
    0.txt路径   原始脚本文件（GB18030 编码）。
    游戏目录    包含 images/bgm/voice/se 的 game 目录（用于校验资源、读取立绘尺寸）。

依赖:
    Pillow（用于读取立绘图片尺寸，计算立绘定位）。

转换要点:
    - 屏幕分辨率 800x450（16:9）。
    - 立绘按 ONScripter lsp2 的中心坐标语义定位（Transform xanchor=0.5）。
    - 背景 4:3 素材居中裁剪显示（bgfit transform）。
    - 语音文件名自动加 voice/ 前缀（由 options.rpy 的 voice_filename_format 完成）。
    - 原脚本个别行是 Shift-JIS（路线选择文字），其余为 GB18030，已单独修正。
    - 一行含多个 [1|说话人|语音] 标签时拆分多句。
"""
import os
import re
import sys

SRC = "/Users/greenhats/Downloads/突然之间发现我已恋上你/assets/0.txt"
GAME_DIR = "/Users/greenhats/Documents/突恋/tulian/game"

W, H_SCREEN = 800, 450

try:
    from PIL import Image
except ImportError:
    Image = None
    print("警告: 未安装 Pillow，立绘尺寸无法读取，立绘 y 定位回退默认值。")

# Shift-JIS 行被 GB18030 误解码产生的乱码 → 修正为中文
ROUTE_FIX = {
    "塺壧儖乕僩": "詠歌路线",
    "椓儖乕僩": "涼路线",
    "堺儖乕僩": "胤路线",
    "朼儖乕僩": "紡路线",
}

img_size = {}

def get_size(fname):
    if fname in img_size:
        return img_size[fname]
    p = os.path.join(GAME_DIR, "images", fname)
    if not os.path.exists(p) or Image is None:
        img_size[fname] = None
        return None
    try:
        im = Image.open(p)
        img_size[fname] = im.size
        return im.size
    except Exception:
        img_size[fname] = None
        return None

voice_files = set()
_voice_dir = os.path.join(GAME_DIR, "voice")
if os.path.isdir(_voice_dir):
    for f in os.listdir(_voice_dir):
        voice_files.add(f.lower())

def voice_path(voice_id):
    v = voice_id.lower() + ".ogg"
    return v if v in voice_files else None

img_exists = {}

def bg_exists(name):
    if name in img_exists:
        return img_exists[name]
    e = os.path.exists(os.path.join(GAME_DIR, "images", name + ".png"))
    img_exists[name] = e
    return e

def resolve_bg(name):
    if bg_exists(name):
        return name
    if name.endswith("_fr") and bg_exists(name[:-3]):
        return name[:-3]
    return None

def clean_inline_text(t):
    t = re.sub(r'\\c0x[0-9a-fA-F]+', '', t)
    t = re.sub(r'\\c[0-9a-fA-F]+', '', t)
    t = t.replace('\\c', '')
    t = t.replace('\\pr', '\\n')
    t = t.replace('\\pc', '')
    t = t.replace('\\p', '')
    t = re.sub(r'\\w\d*', '', t)
    t = re.sub(r'\\f([+-]\d+)', lambda m: "{size=%s}" % m.group(1), t)
    t = t.replace('\\f', '{/size}')
    t = re.sub(r'\\[a-z]\d*', '', t)
    return t

def esc(t):
    return (t.replace('%', '%%')
             .replace('[', '[[')
             .replace('"', '\\"')
             .replace('{', '{{')
             .replace('}', '}}'))

def parse_sprite_name(path):
    base = os.path.basename(path.replace('\\', '/'))
    m = re.match(r'^(.*?)x(\d+)y(\d+)\.png$', base)
    if m:
        return base, int(m.group(2)), int(m.group(3))
    return base, None, None

def main():
    with open(SRC, "rb") as f:
        raw = f.read()
    text = raw.decode("gb18030", errors="replace")
    for k, v in ROUTE_FIX.items():
        text = text.replace(k, v)
    lines = text.split("\n")

    defined_labels = set()
    for l in lines:
        s = l.rstrip("\t\r").strip("\t")
        if s.startswith("*"):
            defined_labels.add(s[1:].strip())

    speaker_ids = {}
    def sid(name):
        if name not in speaker_ids:
            speaker_ids[name] = "n%d" % len(speaker_ids)
        return speaker_ids[name]

    slot_tag = {41: "c41", 42: "c42", 43: "c43"}

    out = []
    def emit(s=""):
        out.append(s)

    seen_labels = {}

    i = 0
    N = len(lines)
    started = False
    menu_pending = None

    while i < N:
        raw_line = lines[i]
        line = raw_line.rstrip("\t\r").strip("\t")

        if line.startswith("*"):
            name = line[1:].strip()
            if name == "L_common00":
                started = True
            if not started:
                i += 1
                continue
            if not name.startswith("L_"):
                i += 1
                continue
            seen_labels[name] = seen_labels.get(name, 0) + 1
            emit_name = name if seen_labels[name] == 1 else ("%s__dup%d" % (name, seen_labels[name]))
            emit("label %s:" % emit_name)
            i += 1
            continue

        if not started:
            i += 1
            continue

        if line.startswith("[1|"):
            parts = []
            pattern = re.compile(r'\[1\|([^|]*)\|([^\]]*)\]([^\[]*)')
            for m in pattern.finditer(line):
                name, voice, txt = m.group(1), m.group(2), m.group(3)
                txt = txt.rstrip('\\').rstrip('\t')
                txt = clean_inline_text(txt)
                txt = re.sub(r'^pl', '', txt)
                parts.append((name, voice, txt))
            for name, voice, txt in parts:
                if not txt.strip():
                    continue
                vp = voice_path(voice) if voice else None
                if vp:
                    emit('    voice "%s"' % vp)
                if name:
                    emit('    %s "%s"' % (sid(name), esc(txt)))
                else:
                    emit('    "%s"' % esc(txt))
            i += 1
            continue

        if line == "nend":
            i += 1
            continue

        m = re.match(r'^bgm "([^"]+)"', line)
        if m:
            emit('    play music "%s"' % m.group(1))
            i += 1
            continue

        m = re.match(r'^dwave 2,"([^"]+)"', line)
        if m:
            emit('    play sound "%s"' % m.group(1))
            i += 1
            continue

        m = re.match(r'^dwave 0,"([^"]+)"', line)
        if m:
            emit('    play sound "%s"' % m.group(1))
            i += 1
            continue

        if line.startswith("dwavestop"):
            i += 1
            continue

        m = re.match(r'^lsp2 56,"image/([^"]+)\.png"', line)
        if m:
            bg = resolve_bg(m.group(1))
            if bg:
                emit('    scene %s at bgfit' % bg)
            else:
                emit('    scene black')
            i += 1
            continue

        m = re.match(r'^lspsr (\d+),"([^"]+)",(\d+),(\d+)', line)
        if m:
            slot = int(m.group(1))
            path = m.group(2)
            x_arg = int(m.group(3))
            y_arg = int(m.group(4))
            base, ax, ay = parse_sprite_name(path)
            tag = slot_tag.get(slot, "c%d" % slot)
            size = get_size(base)
            if size:
                h = size[1]
                if h > 1300:
                    ypos = h // 2 + 20
                else:
                    ypos = h - y_arg + 225
                emit('    show %s as %s at Transform(xanchor=0.5, yanchor=0.5, xpos=%d, ypos=%d)'
                     % (base[:-4], tag, x_arg, ypos))
            else:
                emit('    show %s as %s' % (base[:-4], tag))
            i += 1
            continue

        if line == "cspchar":
            emit("    hide c41")
            emit("    hide c42")
            emit("    hide c43")
            i += 1
            continue

        m = re.match(r'^csp2 (\d+)', line)
        if m:
            slot = int(m.group(1))
            tag = slot_tag.get(slot, "c%d" % slot)
            emit("    hide %s" % tag)
            i += 1
            continue

        m = re.match(r'^goto \*([A-Za-z0-9_]+)', line)
        if m:
            if m.group(1) in defined_labels:
                emit("    jump %s" % m.group(1))
            else:
                emit("    # [bad jump] %s (target undefined, falling through)" % m.group(1))
            i += 1
            continue

        m = re.match(r'^cselect2 "([^"]+)","\*([^"]+)","([^"]+)","\*([^"]+)"', line)
        if m:
            menu_pending = (m.group(1), m.group(2), m.group(3), m.group(4))
            i += 1
            continue

        if line == "goto $1" and menu_pending:
            a, la, b, lb = menu_pending
            emit("    menu:")
            emit('        "%s":' % esc(a))
            emit("            jump %s" % la)
            emit('        "%s":' % esc(b))
            emit("            jump %s" % lb)
            menu_pending = None
            i += 1
            continue

        if line.startswith("pc"):
            txt = line[2:].rstrip('\\').rstrip('\t')
            txt = clean_inline_text(txt)
            emit('    centered "%s"' % esc(txt))
            i += 1
            continue

        m = re.match(r'^f([+-]\d+)(.*)$', line)
        if m:
            txt = m.group(2).rstrip('\\').rstrip('\t')
            emit('    "{size=%s}%s{/size}"' % (m.group(1), esc(txt)))
            i += 1
            continue

        m = re.match(r'^wait (\d+)', line)
        if m:
            emit("    pause %g" % (int(m.group(1)) / 1000.0))
            i += 1
            continue

        m = re.match(r'^print 10,(\d+)', line)
        if m:
            ms = int(m.group(1))
            if ms >= 100:
                emit("    with dissolve")
            i += 1
            continue

        if line == "end":
            emit("    return")
            i += 1
            continue

        if line == "reset":
            emit("    return")
            i += 1
            continue

        if line == "":
            i += 1
            continue

        emit("    # [unhandled] %s" % line)
        i += 1

    char_defs = ['define %s = Character("%s")' % (cid, name) for name, cid in speaker_ids.items()]

    out_path = os.path.join(GAME_DIR, "script.rpy")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("# 转换自 0.txt (NScripter)\n\n")
        for d in char_defs:
            f.write(d + "\n")
        f.write('\ntransform bgfit:\n')
        f.write('    align (0.5, 0.5)\n\n')
        f.write("label start:\n")
        f.write("    jump L_common00\n\n")
        f.write("\n".join(out))
        f.write("\n")

    print("speakers:", len(speaker_ids))
    print("lines emitted:", len(out))
    print("output:", out_path)
    print("done")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        SRC = sys.argv[1]
    if len(sys.argv) > 2:
        GAME_DIR = sys.argv[2]
    main()
