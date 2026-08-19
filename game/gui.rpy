################################################################################
## Initialization
################################################################################

## The init offset statement causes the init code in this file to run before
## init code in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(800, 450)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True


################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#f0609c'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#cccccc'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#ff8fb8'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#ffffff'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#5555557f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#4d3040'
define gui.hover_muted_color = '#7a4d60'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "default.ttf"

## The font used for character names.
define gui.name_text_font = "default.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "default.ttf"

## The size of normal dialogue text.
define gui.text_size = 18

## The size of character names.
define gui.name_text_size = 20

## The size of text in the game's user interface.
define gui.interface_text_size = 18

## The size of labels in the game's user interface.
define gui.label_text_size = 20

## The size of text on the notify screen.
define gui.notify_text_size = 14

## The size of the game's title.
define gui.title_text_size = 30


## Main and Game Menus #########################################################

## The images used for the main and game menus.
define gui.main_menu_background = "images/sys_title00001.png"
define gui.game_menu_background = "images/bg1000e1x0y96.png"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 105

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
define gui.name_xpos = 110
define gui.name_ypos = -76

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.0

## The width, height, and borders of the box containing the character's name.
define gui.namebox_width = 220
define gui.namebox_height = None

define gui.namebox_borders = Borders(5, 5, 5, 5)

define gui.namebox_tile = False


## The placement of dialogue relative to the textbox.
define gui.dialogue_xpos = 168
define gui.dialogue_ypos = 28

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 580

## The horizontal alignment of the dialogue text.
define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################

define gui.button_width = None
define gui.button_height = None

define gui.button_borders = Borders(4, 4, 4, 4)

define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font

define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons.

define gui.radio_button_borders = Borders(25, 4, 4, 4)

define gui.check_button_borders = Borders(25, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 12
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 620
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"


## File Slot Buttons ###########################################################

define gui.slot_button_width = 165
define gui.slot_button_height = 105
define gui.slot_button_borders = Borders(10, 4, 10, 4)
define gui.slot_button_text_size = 12
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color

define config.thumbnail_width = 145
define config.thumbnail_height = 70

define gui.file_slot_cols = 2
define gui.file_slot_rows = 3


## Positioning and Spacing #####################################################

define gui.navigation_xpos = 20

define gui.skip_ypos = 10

define gui.notify_ypos = 30

define gui.choice_spacing = 6

define gui.navigation_spacing = 2

define gui.pref_spacing = 6

define gui.pref_button_spacing = 0

define gui.page_spacing = 0

define gui.slot_spacing = 6

define gui.main_menu_text_xalign = 0.0


## Frames ######################################################################

define gui.frame_borders = Borders(20, 8, 20, 8)

define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

define gui.skip_frame_borders = Borders(16, 5, 50, 5)

define gui.notify_frame_borders = Borders(16, 5, 40, 5)

define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################

define gui.bar_size = 24
define gui.scrollbar_size = 10
define gui.slider_size = 20

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

define gui.unscrollable = "hide"


## History #####################################################################

define config.history_length = 250

define gui.history_height = 90

define gui.history_name_xpos = 90
define gui.history_name_ypos = 0
define gui.history_name_width = 90
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 105
define gui.history_text_ypos = 5
define gui.history_text_width = 560
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################

define gui.nvl_borders = Borders(0, 10, 0, 20)

define gui.nvl_height = 70

define gui.nvl_spacing = 6

define gui.nvl_name_xpos = 250
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 100
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 265
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 400
define gui.nvl_text_xalign = 0.0

define gui.nvl_thought_xpos = 140
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 500
define gui.nvl_thought_xalign = 0.0

define gui.nvl_button_xpos = 265
define gui.nvl_button_xalign = 0.0

## Localization ################################################################

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 20
        gui.name_text_size = 22
        gui.notify_text_size = 16
        gui.interface_text_size = 20
        gui.button_text_size = 20
        gui.label_text_size = 22

        ## Adjust the location of the textbox.
        gui.textbox_height = 130
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 700

        ## Change the size and spacing of items in the game menu.
        gui.choice_button_width = 700

        gui.navigation_spacing = 10
        gui.pref_button_spacing = 6

        gui.history_height = 110
        gui.history_text_width = 500

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 100

        gui.nvl_name_width = 180
        gui.nvl_name_xpos = 190

        gui.nvl_text_width = 600
        gui.nvl_text_xpos = 200
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 700
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 700
        gui.nvl_button_xpos = 20

        ## Quick buttons.
        gui.quick_button_text_size = 16
