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
    [1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,0,0,0,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Cursor Img.
CURSOR_IMG = pygame.transform.scale(pygame.image.load('vfx/libresprite_files/cursor.png'), (16*1.5, 16*1.5))

# Background.
BACKGROUND_PARTICLE_IMAGE = pygame.transform.scale(pygame.image.load('vfx/particles/background_particle.png'), (16*0.3, 16*0.3))  
BACKGROUND_MOON_IMAGE = pygame.transform.scale(pygame.image.load('vfx/libresprite_files/background_moon.png'), (16*4, 16*4))

# Gun Images.
SIMPLE_GUN_SIZE = (16*1.8, 10*1.8)
SIMPLE_GUN_IMAGE = pygame.transform.scale(pygame.image.load('vfx/weapons/simple_gun.png'), SIMPLE_GUN_SIZE)
SIMPLE_GUN_BULLET_SIZE = (16*0.5, 16*0.5)
SIMPLE_GUN_BULLET_IMAGE = pygame.transform.scale(pygame.image.load('vfx/weapons/simple_gun_bullet.png'), SIMPLE_GUN_BULLET_SIZE)
SIMPLE_GUN_BULLET_DAMAGE = 0
SIMPLE_GUN_BULLET_SPEED = 0.5
SIMPLE_GUN_MAX_BULLET_SHOOT = 1
SIMPLE_GUN_BULLET_TIMER = 0.5

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
                                    is_reverse=(False, False))
TILE_IMAGES.append(SPIKE_IMAGE)

# PLAYER
PLAYER_HORIZONTAL_SPEED = 5
PLAYER_JUMP_FORCE = -20
PLAYER_MASS = 4
PLAYER_STARTING_POS = (16*2, 16*2)
PLAYER_HEALTH = 10
PLAYER_DAMAGE = 1
PLAYER_DAMAGE_PARTICLE_IMAGE = pygame.transform.scale(pygame.image.load('vfx/particles/damage_particle.png'), (16*0.5, 16*0.5))

# PLAYER ANIMATION.
PLAYER_ANIMATION = {
    'idle': [generate_pygame_image(dir='vfx/player/idle', resize=(16*2, 16*2), is_reverse=(False, False)), 0.1],
    'run_right': [generate_pygame_image(dir='vfx/player/run', resize=(16*2, 16*2), is_reverse=(False, False)), 0.3],
    'run_left': [generate_pygame_image(dir='vfx/player/run', resize=(16*2, 16*2), is_reverse=(True, False)), 0.3],
    'jump_right': [generate_pygame_image(dir='vfx/player/jump', resize=(16*2, 16*2), is_reverse=(False, False)), 0.1],
    'jump_left': [generate_pygame_image(dir='vfx/player/jump', resize=(16*2, 16*2), is_reverse=(True, False)), 0.1],
    'damage': [generate_pygame_image(dir='vfx/player/damage', resize=(16*2, 16*2), is_reverse=(False, False)), 0.5],
    'die_1': [generate_pygame_image(dir='vfx/player/die_1', resize=(16*2, 16*2), is_reverse=(False, False)), 0.1],
    'die_2': [generate_pygame_image(dir='vfx/player/die_2', resize=(16*2, 16*2), is_reverse=(False, False)), 0.05],
}

# FLYING ENEMY.
# FLYING ENEMY ANIMATION.
FLYING_ENEMY_ANIMATION = {
    'idle_right': [generate_pygame_image(dir='vfx/enemies/flying_enemy/idle', resize=(16*2, 16*2), is_reverse=(False, False)), 0.1],
    'idle_left': [generate_pygame_image(dir='vfx/enemies/flying_enemy/idle', resize=(16*2, 16*2), is_reverse=(True, False)), 0.1],
    'damage_right': [generate_pygame_image(dir='vfx/enemies/flying_enemy/damage', resize=(16*2, 16*2), is_reverse=(False, False)), 0.1],
    'damage_left': [generate_pygame_image(dir='vfx/enemies/flying_enemy/damage', resize=(16*2, 16*2), is_reverse=(True, False)), 0.1]
}

HEALTHBAR_IMAGE = pygame.transform.scale(pygame.image.load('vfx/libresprite_files/health_bar.png'), (96*2, 32*2))