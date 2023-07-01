# Importing Libraries.
import pygame
from pygame.locals import *
import time

# Importing Local Modules.
from .settings import *
from .player import Player
from .functions import animate, key_handler, collision_handler
from .tilemap import Tilemap

# Initialising Pygame.
pygame.init()

class GameManager:
    def __init__(self):
        # width and height for the screen.
        self.width = WIDTH
        self.height = HEIGHT

        # Setting up Screen.
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_icon(PLAYER_IDLE_RIGHT_IMAGES[0])

        # Setting up clock for FPS.
        self.clock = pygame.time.Clock()
        self.dt = 0

        # Loading all the variables.
        self.load()

    def load(self) -> None:
        '''
        Loads all the variables.
        '''
        self.player = Player(PLAYER_IDLE_RIGHT_IMAGES[0], PLAYER_STARTING_POS[0], PLAYER_STARTING_POS[1])
        self.player.mass = PLAYER_MASS # Setting player's mass.
        self.tilemap = Tilemap(map_data=level,
                              tile_size=TILE_SIZE,
                              tiles=TILE_IMAGES)

    def rendering(self) -> None:
        '''
        This method will handle all the rendering stuff.
        '''

        if self.player.dx > 0: # Right Run.
            animate(self.player, PLAYER_RUN_RIGHT_IMAGES, PLAYER_RUN_SPEED)
        elif self.player.dx < 0: # Left Run.
            animate(self.player, PLAYER_RUN_LEFT_IMAGES, PLAYER_RUN_SPEED)
        else: # Idle.
            animate(self.player, PLAYER_IDLE_RIGHT_IMAGES, PLAYER_IDLE_SPEED)
        
        # Rendering Tiles.
        self.tilemap.draw(self.screen)

        # Rendering Player.
        self.player.draw(self.screen)

    def computing(self) -> None:
        '''
        This method will handle all the computing/calculations stuff.
        '''

        # Setting delta x to 0 or else the speed would increase continuously.
        self.player.dx = 0
        self.player.rect.y += self.player.dy
        collisionY, hitY = collision_handler(self.player, self.tilemap.tiles_group, 'Y')
        # We need to write self.player.dy here because else it will 
        # basically be 0 everytime and no collisions will be detected.
        self.player.dy = 0
        if collisionY['DOWN'] != True:
            self.player.apply_gravity(GRAVITY)

        keys = key_handler()
        if keys['LEFT']:
            self.player.dx += -PLAYER_HORIZONTAL_SPEED
        if keys['RIGHT']:
            self.player.dx += PLAYER_HORIZONTAL_SPEED
        if keys['UP']:
            if collisionY['DOWN']:
                pass

        self.player.rect.x += self.player.dx
        collisionX, hitX = collision_handler(self.player, self.tilemap.tiles_group, 'X')

    def run(self) -> None:
        '''
        This method runs/updates the game.
        '''
        running = True
        while running:
            # Filling screen with background color and displaying FPS.
            self.screen.fill(BACKGROUND_COLOR)

            self.computing()
            self.rendering()

            pygame.display.set_caption(str(round(self.clock.get_fps())))

            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                    running = False

            # Updating screen.
            self.clock.tick(FPS)
            pygame.display.update()
            pygame.display.flip()