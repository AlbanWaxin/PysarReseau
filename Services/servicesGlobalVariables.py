import pyautogui

#DEFAULT_SCREEN_WIDTH = user32.GetSystemMetrics(0)
#DEFAULT_SCREEN_HEIGHT = user32.GetSystemMetrics(1)
DEFAULT_SCREEN_WIDTH,DEFAULT_SCREEN_HEIGHT =pyautogui.size()
MIDDLE = (DEFAULT_SCREEN_WIDTH/2,DEFAULT_SCREEN_HEIGHT/2)
TITLE = "Pysar"

SPRITE_PATH = "Assets/sprites/C32/"
LOGO_PATH = SPRITE_PATH + "logo.png"
DEFAULT_FPS =60

SPRITE_SCALING = 1/2
SCALE_MIN = SPRITE_SCALING/2
SCALE_MAX = 1.5 * SPRITE_SCALING

TILE_COUNT = 40
TILE_WIDTH = 58*2
TILE_HEIGHT = 29*2

MAP_WIDTH = TILE_WIDTH*TILE_COUNT
MAP_HEIGHT =TILE_HEIGHT*TILE_COUNT

LAYER1 = "grass"
LAYER2 = "hills"
LAYER3 = "trees"
LAYER4 = "roads"
LAYER5 = "buildings"

FONT_WIDTH=16
FONT_HEIGHT=22

WALKER_UNIT = 5

IMMIGRANT_INSTALLED = 1
CITIZEN_ARRIVED = 2
CITIZEN_IS_OUT = 3
ARRIVED_SIGNAL = 10
