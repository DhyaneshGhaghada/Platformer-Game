# Importing Libraries.
import pygame
from pygame.locals import *
import random

# Importing Local Modules.
from .settings import *
from .player import Player
from .tilemap import Tilemap
from .functions import change_cursor_img
from .background import Background
from .enemies.flying_enemy import FlyingEnemySystem
from .UI_Lib.textbox import Textbox

# Initialising Pygame.
pygame.init()

# Initialsing Pygame For Music.
pygame.mixer.init()

class GameManager:
    def __init__(self):
        # width and height for the screen.
        self.width = WIDTH
        self.height = HEIGHT

        # Setting up Screen.
        self.window = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.Surface(self.window.get_size())
        self.screen_rect = self.screen.get_rect()
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

        self.flying_enemy = FlyingEnemySystem(self.player, self)

        self.score = Textbox('vfx/fonts/Delicious_Handrawn/DeliciousHandrawn-Regular.ttf', 40)

        self.is_screenshake = False
        self.screenshake_timer = 5
        self.screenshake_intensity = 2

        pygame.mixer.music.load('sfx/main_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)


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

        # Rendering Score.
        self.score.draw_text(self.screen)

        # Rendering Cursor.
        change_cursor_img(self.screen, CURSOR_IMG)

    def computing(self) -> None:
        '''
        This method will handle all the computing/calculations stuff.
        '''
        self.player.update(self.tilemap.tiles_group, self.tilemap.spikes_group)
        self.player.enemy_damage(self.flying_enemy.flying_enemy_group)

        self.score.clear_text()
        self.score.create_text(f'Score - {self.player.score}', (255, 255, 255), (1000, 5))

        # Screen shake when enemy dies.
        if self.is_screenshake:
            self.screenshake_timer -= 0.1
            self.screen_rect.x, self.screen_rect.y = 0, 0
            self.screen_rect.x += random.uniform(-1, 1)*self.screenshake_intensity
            self.screen_rect.y += random.uniform(-1, 1)*self.screenshake_intensity
            if self.screenshake_timer <= 0:
                self.is_screenshake = False
                self.screenshake_timer = 5

    def run(self) -> None:
        '''
        This method runs/updates the game.
        '''
        running = True
        while running:
            # Filling screen with background color and displaying FPS.
            self.window.fill(BACKGROUND_COLOR)
            self.window.blit(self.screen, self.screen_rect)
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