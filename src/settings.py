from .functions import generate_pygame_image


# Screen width and height.
WIDTH = 800
HEIGHT = 600

# Frames Per Second
FPS = 60

# Background Color
BACKGROUND_COLOR = (0, 0, 0)

# Universal Gravity.
GRAVITY = 2

# Level
level = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


# TILE IMAGES.
TILE_DIR = 'vfx/tiles'
TILE_SIZE = 16*2
TILE_IMAGES = generate_pygame_image(dir=TILE_DIR,
                                    resize=(TILE_SIZE, TILE_SIZE),
                                    is_reverse=False)

# PLAYER
PLAYER_HORIZONTAL_SPEED = 5
PLAYER_MASS = 4
PLAYER_STARTING_POS = (16*2, 16*2)
# PLAYER IMAGES.
# Player Idle.
PLAYER_IDLE_DIR = "vfx/player/idle"
PLAYER_IDLE_SPEED = 0.1
PLAYER_IDLE_RIGHT_IMAGES = generate_pygame_image(dir=PLAYER_IDLE_DIR,
                                                resize=(16*2,16*2),
                                                is_reverse=False)

# Player Run.
# RIGHT
PLAYER_RUN_DIR = "vfx/player/run"
PLAYER_RUN_SPEED = 0.3
PLAYER_RUN_RIGHT_IMAGES = generate_pygame_image(dir=PLAYER_RUN_DIR,
                                                resize=(16*2,16*2),
                                                is_reverse=False)
# LEFT
PLAYER_RUN_LEFT_IMAGES = generate_pygame_image(dir=PLAYER_RUN_DIR,
                                                resize=(16*2,16*2),
                                                is_reverse=True)