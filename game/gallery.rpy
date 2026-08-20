# -*- coding: utf-8 -*-
# 剧情鉴赏（H 场景直接回放）
# 入口：主菜单 -> 剧情鉴赏；场景经由 Ren'Py Replay 机制从 gallery_scenes.rpy 独立副本播放。
# 所有场景初始即解锁；演完场景（return）自动返回鉴赏菜单。

init python:
    # 路线与场景映射：
    #   每条 = (路线名, [ (封面图, 序号, 独立场景标签), ... ])
    # 封面图取场景开场的第一张 CG（images/ 下 799x449 的 ev 图）。
    gallery_routes = [
        ("詠歌", [
            ("ev1100a", 1, "gallery_eika_ind03_ero1"),
            ("ev1102a", 2, "gallery_eika_ind04_ero2"),
            ("ev1103a", 3, "gallery_eika_ind07_ero3"),
            ("ev1008a", 4, "gallery_eika_ind08_ero4"),
            ("ev1111a", 5, "gallery_eika_ind09_ero5"),
            ("ev1109a", 6, "gallery_eika_ind10_ero6"),
            ("ev1110b", 7, "gallery_eika_ind12_ero7"),
            ("ev1116a", 8, "gallery_eika_ind14_ero8"),
        ]),
        ("涼", [
            ("ev0101a", 1, "gallery_ryo_ind12_ero1"),
            ("ev0102a", 2, "gallery_ryo_ind12_ero2"),
            ("ev0105a", 3, "gallery_ryo_ind13_ero3"),
            ("ev0108a", 4, "gallery_ryo_ind14_ero4"),
            ("ev0109a", 5, "gallery_ryo_ind16_ero5"),
        ]),
        ("胤", [
            ("ev2002k", 1, "gallery_tane_ind01_ero1"),
            ("ev2101a", 2, "gallery_tane_ind05_ero2"),
            ("ev2007a", 3, "gallery_tane_ind06_ero3"),
            ("ev2103d", 4, "gallery_tane_ind07_ero4"),
            ("ev2104a", 5, "gallery_tane_ind08_ero5"),
            ("ev2106b", 6, "gallery_tane_ind09_ero6"),
            ("ev2108b", 7, "gallery_tane_ind10_ero7"),
        ]),
        ("紡", [
            ("ev3101a", 1, "gallery_tmg_ind05_ero1"),
            ("ev3103a", 2, "gallery_tmg_ind07_ero2"),
            ("ev3105a", 3, "gallery_tmg_ind09_ero3"),
            ("ev3107a", 4, "gallery_tmg_ind12_ero4"),
        ]),
    ]

    # 序号 -> 封面图（供显示用）
    gallery_thumbs = {}
    for _rname, _scenes in gallery_routes:
        for _cover, _num, _lab in _scenes:
            gallery_thumbs[_lab] = _cover


screen gallery():

    tag menu

    default g_route = "詠歌"

    use game_menu(_("剧情鉴赏")):

        fixed:

            # 角色选择 banner
            frame:
                style "gallery_banner"
                xalign 0.5
                ypos 10

                hbox:
                    spacing 6
                    for rname, _scenes in gallery_routes:
                        textbutton rname:
                            style "gallery_banner_button"
                            selected (g_route == rname)
                            action SetScreenVariable("g_route", rname)

            python:
                cur = []
                for rname, scenes in gallery_routes:
                    if rname == g_route:
                        cur = scenes
                        break

            # 场景封面网格（仿存档位，点击即播放）
            viewport:
                xalign 0.5
                xoffset 55
                ypos 72
                xsize 520
                ysize 320
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 7

                    for k in range(0, len(cur), 3):

                        hbox:
                            spacing 8

                            for cover, cnum, lab in cur[k:k+3]:

                                button:
                                    style "gallery_slot_button"
                                    action Replay(lab, locked=False)

                                    has fixed

                                    add cover at fit_gallery_thumb

                                    text ("第%d场" % cnum):
                                        style "gallery_slot_text"
                                        xalign 0.5
                                        yalign 1.0


transform fit_gallery_thumb:
    xysize (124, 70)
    align (0.5, 0.5)


style gallery_banner:
    xsize 420
    background "#00000066"
    padding (8, 5)

style gallery_banner_button:
    xsize 70
    ysize 22
    background "#22222288"
    hover_background "#f0609c88"
    selected_background "#f0609c"

style gallery_banner_button_text:
    xalign 0.5
    yalign 0.5
    size 15
    color "#ffffff"
    hover_color "#ffffff"
    selected_color "#ffffff"

style gallery_slot_button:
    xsize 132
    ysize 80
    padding (4, 5)
    xfill False
    yfill False

style gallery_slot_text:
    size 12
    color "#ffffff"
    yoffset -4
    outlines [ (2, "#00000088", 0, 0) ]