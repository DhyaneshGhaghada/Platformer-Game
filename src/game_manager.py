# Importing Libraries.
import pygame
from pygame.locals import *

# Importing Local Modules.
from .settings import *
from .player import Player
from .tilemap import Tilemap
from .gun import Simple_Gun
from .functions import change_cursor_img
from .background import Background

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
        self.player.mass = PLAYER_MASS # Setting player's mass.

        self.tilemap = Tilemap(map_data=level,
                              tile_size=TILE_SIZE,
                              tiles=TILE_IMAGES)

        self.gun = Simple_Gun(self.player, SIMPLE_GUN_IMAGE, SIMPLE_GUN_BULLET_IMAGE)
        self.gun.bullet_damage = SIMPLE_GUN_BULLET_DAMAGE
        self.gun.bullet_speed = SIMPLE_GUN_BULLET_SPEED
        self.gun.bullet_timer = SIMPLE_GUN_BULLET_TIMER
        self.gun.max_bullet_shoot = SIMPLE_GUN_MAX_BULLET_SHOOT
        self.gun.create_particles(SIMPLE_GUN_PARTICLE_IMAGE, SIMPLE_GUN_PARTICLE_UPFORCE, SIMPLE_GUN_PARTICLE_GRAVITY, SIMPLE_GUN_PARTICLE_TIMERSPEED, SIMPLE_GUN_PARTICLE_MAX)

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

        # Rendering Gun.
        self.gun.draw(self.screen)

        # Rendering Cursor.
        change_cursor_img(self.screen, CURSOR_IMG)

    def computing(self) -> None:
        '''
        This method will handle all the computing/calculations stuff.
        '''
        self.player.update(self.tilemap.tiles_group, self.tilemap.spikes_group)
        self.gun.rotate_gun_on_mouse_pos()
        self.gun.update_bullet_status(self.tilemap.tiles_group)

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