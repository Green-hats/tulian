# -*- coding: utf-8 -*-
# 突然之间发现我已恋上你 — Ren'Py options

define config.name = _("突然之间发现我已恋上你")
define config.screen_width = 800
define config.screen_height = 450

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = None

# 关闭窗口时直接退出，不弹确认框（legacy 界面缺少 yesno_prompt）
define config.quit_action = Quit(confirm=False)

define build.name = "ikikoi"

# 使用游戏自带的 default.ttf 字体（支持中文）
init python:
    style.default.font = "default.ttf"
