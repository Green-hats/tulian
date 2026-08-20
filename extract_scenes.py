#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 script.rpy 中抽取所有 H 场景（label L_*_eroN）到独立的 game/gallery_scenes.rpy。

原则：
  - 不改动 script.rpy（原场景保留，正常剧情流程不受影响，存档零影响）。
  - 抽取出的场景重命名为 gallery_<原名>（去掉 L_ 前缀），复制其语句。
  - 区块结尾的 "jump L_xxx" 处理：
      * 目标仍是另一个 ero 场景 -> 改跳转到对应的 gallery_ 副本（保持连续场景）。
      * 目标是普通章节标签     -> 改写为 return（鉴赏时演完本场景即返回）。
      * 原本就是 return        -> 保持不变。

用法::

    python3 extract_scenes.py [script.rpy路径] [输出路径]
"""
import re
import sys

SRC = "game/script.rpy"
OUT = "game/gallery_scenes.rpy"


def gallery_name(orig):
    """L_eika_ind03_ero1 -> gallery_eika_ind03_ero1"""
    return "gallery_" + orig[len("L_"):]


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else SRC
    out = sys.argv[2] if len(sys.argv) > 2 else OUT

    with open(src, encoding="utf-8") as f:
        lines = f.read().split("\n")

    # 收集所有 label 行号（含大文件里的 ero 标签本身）
    label_lines = [
        (i, m.group(1))
        for i, l in enumerate(lines)
        if (m := re.match(r"^label (L_\S+):", l))
    ]

    ero_names = [
        name
        for _, name in label_lines
        if re.match(r"^L_.*ero\d+$", name)
    ]
    ero_set = set(ero_names)

    blocks = []
    for i, name in label_lines:
        if name not in ero_set:
            continue
        nxt = next(
            (j for j, _ in label_lines if j > i), len(lines)
        )
        body = lines[i + 1:nxt]

        # 抽取副本：逐行复制，处理结尾跳转
        new_body = []
        idx = 0
        while idx < len(body):
            line = body[idx]

            # 清理转换遗留的 "cspchar" 伪台词（原文中的 cspchar 指令误转成台词）
            if line.strip() == '"cspchar"':
                new_body.append("    hide c41")
                new_body.append("    hide c42")
                new_body.append("    hide c43")
                idx += 1
                continue

            m = re.match(r"jump (\S+)", line.strip())
            if m and idx == len(body) - 1:
                tgt = m.group(1)
                if tgt in ero_set:
                    new_body.append("    jump %s" % gallery_name(tgt))
                else:
                    new_body.append("    return")
                idx += 1
                continue

            new_body.append(line)
            idx += 1

        blocks.append((name, new_body))

    with open(out, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("# 剧情鉴赏独立场景（由 extract_scenes.py 从 script.rpy 自动抽取）\n")
        f.write("# 原 script.rpy 保持不变；此处为副本，结尾 jump 已改写为 return。\n\n")
        for name, body in blocks:
            f.write("label %s:\n" % gallery_name(name))
            for line in body:
                f.write(line + "\n")
            f.write("\n")

    print("抽取 %d 个场景 -> %s" % (len(blocks), out))


if __name__ == "__main__":
    main()