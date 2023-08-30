# Importing Libraries.
import pygame
from pygame.locals import *

# Importing Local Modules.
from .settings import *
from .player import Player
from .tilemap import Tilemap
from .functions import change_cursor_img
from .background import Background
from .enemies import FlyingEnemySystem

# Initialising Pygame.
pygame.init()

class GameManager:
    def __init__(self):
        # width and height for the screen.
        self.width = WIDTH
        self.height = HEIGHT

        # Setting up Screen.
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_icon(PLAYER_ANIMATION['idle'][0][0])

        # Setting up clock for FPS.
        self.clock = pygame.time.Clock()
        self.dt = 0

        pygame.mouse.set_visible(False)

        # Loading all the variables.
        self.load()

    def load(self) -> None:
        '''
        Loads all the variables/objects.
        '''
        
        self.background = Background(BACKGROUND_PARTICLE_IMAGE)

        self.player = Player(PLAYER_ANIMATION['idle'][0][0], PLAYER_STARTING_POS[0], PLAYER_STARTING_POS[1])

        self.tilemap = Tilemap(map_data=level,
                              tile_size=TILE_SIZE,
                              tiles=TILE_IMAGES)

        self.flying_enemy = FlyingEnemySystem(self.player, self.tilemap.tiles_group)


    def rendering(self) -> None:
        '''
        This method will handle all the rendering stuff.
        '''

        # Rendering Background.
        self.background.update_particles(self.screen)
        
        # Rendering Tiles.
        self.tilemap.draw(self.screen)

        # Rendering Player.
        self.player.draw(self.screen)

        # Rendering and Updating Flying Enemies.
        self.flying_enemy.update_enemy(self.screen)

        # Rendering Cursor.
        change_cursor_img(self.screen, CURSOR_IMG)

    def computing(self) -> None:
        '''
        This method will handle all the computing/calculations stuff.
        '''
        self.player.update(self.tilemap.tiles_group, self.tilemap.spikes_group)

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