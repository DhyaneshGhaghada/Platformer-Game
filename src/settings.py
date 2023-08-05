import pygame

from .functions import generate_pygame_image


# Screen width and height.
WIDTH = 1184
HEIGHT = 576

# Frames Per Second
FPS = 60

# Background Color
BACKGROUND_COLOR = (0, 0, 0)

# Universal Gravity.
GRAVITY = 0.8

# Level
level = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Cursor Img.
CURSOR_IMG = pygame.transform.scale(pygame.image.load('vfx/libresprite_files/cursor.png'), (16*1.5, 16*1.5))

# Background.
BACKGROUND_PARTICLE_IMAGE = pygame.transform.scale(pygame.image.load('vfx/particles/background_particle.png'), (16*0.3, 16*0.3))  

# Gun Images.
SIMPLE_GUN_SIZE = (16*1.8, 10*1.8)
SIMPLE_GUN_IMAGE = pygame.transform.scale(pygame.image.load('vfx/weapons/simple_gun.png'), SIMPLE_GUN_SIZE)
SIMPLE_GUN_BULLET_SIZE = (16*0.5, 16*0.5)
SIMPLE_GUN_BULLET_IMAGE = pygame.transform.scale(pygame.image.load('vfx/weapons/simple_gun_bullet.png'), SIMPLE_GUN_BULLET_SIZE)
SIMPLE_GUN_BULLET_DAMAGE = 0
SIMPLE_GUN_BULLET_SPEED = 0.5
SIMPLE_GUN_MAX_BULLET_SHOOT = 1
SIMPLE_GUN_BULLET_TIMER = 2

SIMPLE_GUN_PARTICLE_SIZE = 4
SIMPLE_GUN_PARTICLE_IMAGE = pygame.transform.scale(pygame.image.load('vfx/particles/particle1.png'), (SIMPLE_GUN_PARTICLE_SIZE, SIMPLE_GUN_PARTICLE_SIZE))
SIMPLE_GUN_PARTICLE_UPFORCE = -2
SIMPLE_GUN_PARTICLE_GRAVITY = 0.09
SIMPLE_GUN_PARTICLE_TIMERSPEED = 0.2
SIMPLE_GUN_PARTICLE_MAX = 2

# Spikes.
SPIKE_IMAGE = pygame.transform.scale(pygame.image.load('vfx/libresprite_files/spikes.png'), (16*2, 5*2))

# TILE IMAGES.
TILE_DIR = 'vfx/tiles'
TILE_SIZE = 16*2
TILE_IMAGES = generate_pygame_image(dir=TILE_DIR,
                                    resize=(TILE_SIZE, TILE_SIZE),
                                    is_reverse=False)
TILE_IMAGES.append(SPIKE_IMAGE)

# PLAYER
PLAYER_HORIZONTAL_SPEED = 5
PLAYER_JUMP_FORCE = -20
PLAYER_MASS = 4
PLAYER_STARTING_POS = (16*2, 16*2)
# PLAYER ANIMATION IMAGES.
# Player Idle.
PLAYER_IDLE_DIR = "vfx/player/idle"
PLAYER_IDLE_SPEED = 0.1
PLAYER_IDLE_IMAGES = generate_pygame_image(dir=PLAYER_IDLE_DIR,
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

# JUMP
PLAYER_JUMP_DIR = "vfx/player/jump"
PLAYER_JUMP_SPEED = 0.1
PLAYER_JUMP_RIGHT_IMAGES = generate_pygame_image(dir=PLAYER_JUMP_DIR,
                                                resize=(16*2,16*2),
                                                is_reverse=False)
# LEFT
PLAYER_JUMP_LEFT_IMAGES = generate_pygame_image(dir=PLAYER_JUMP_DIR,
                                                resize=(16*2,16*2),
                                                is_reverse=True)