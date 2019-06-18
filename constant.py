from screeninfo import get_monitors

for m in get_monitors():
    pass

SCREEN_WIDTH = m.width
SCREEN_HEIGHT = m.height
SCREEN_RESOLUTION = int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)

# Colors
COLOR_RGB_BLACK = 0, 0, 0,
