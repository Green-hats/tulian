## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game.
define config.name = _("突然之间发现我已恋上你")


## Determines if the title given above is shown on the main menu screen.
define gui.show_name = False


## 默认界面语言（使用 tl/chinese 翻译覆盖内置英文界面）
define config.language = "chinese"


## The version of the game.
define config.version = "1.0"


## Text that is placed on the game's about screen.
define gui.about = _("突然之间发现我已恋上你\n\nNScripter 脚本转 Ren'Py 移植版")


## A short name for the game used for executables and directories in the built
## distribution.
define build.name = "tulian"


## Sounds and music ############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## 语音文件放在 voice/ 子目录下，自动加上前缀。
define config.voice_filename_format = "voice/{filename}"


## Transitions #################################################################

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## A transition that is used after a game has been loaded.
define config.after_load_transition = None


## Used when entering the main menu after the game has ended.
define config.end_game_transition = None


## Window management ###########################################################

define config.window = "auto"


## Transitions used to show and hide the dialogue window
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

default preferences.text_cps = 50

default preferences.afm_time = 15


## Save directory ##############################################################

define config.save_directory = "tulian-ikikoi"


## Icon ########################################################################

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################

init python:

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
