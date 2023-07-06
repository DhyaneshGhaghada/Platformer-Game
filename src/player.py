import pygame

from .functions import collision_handler, key_handler, animate
from .settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img: pygame.Surface, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.get_rect().x, self.image.get_rect().y = x, y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.dx = 0
        self.dy = 0
        self.current_sprite = 0
        self.mass = 1
        self.in_ground = False

    def movement(self, tiles: pygame.sprite.AbstractGroup) -> None:
        keys = key_handler()

        # Horizontal Movement.
        if keys['LEFT']:
            self.dx += -PLAYER_HORIZONTAL_SPEED
        elif keys['RIGHT']:
            self.dx += PLAYER_HORIZONTAL_SPEED

        self.rect.x += self.dx
        self.collisionX = collision_handler(self, tiles, 'X')
        self.animation('X')
        self.dx = 0

        # Vertical Movement.
        if keys['UP'] and self.in_ground == True:
            self.dy = PLAYER_JUMP_FORCE
            self.in_ground = False
        self.dy += GRAVITY

        self.rect.y += self.dy
        self.collisionY = collision_handler(self, tiles, 'Y')
        self.animation('Y')
        if self.collisionY['DOWN']:
            self.in_ground = True

    def animation(self, direction: str) -> None:
        if direction == 'X' and self.in_ground == True:
            if self.dx > 0:
                animate(self, PLAYER_RUN_RIGHT_IMAGES, PLAYER_RUN_SPEED)
            elif self.dx < 0:
                animate(self, PLAYER_RUN_LEFT_IMAGES, PLAYER_RUN_SPEED)
            else:
                animate(self, PLAYER_IDLE_IMAGES, PLAYER_IDLE_SPEED)
        elif direction == 'Y' and self.in_ground == False:
            if self.dx >= 0:
                animate(self, PLAYER_JUMP_RIGHT_IMAGES, PLAYER_JUMP_SPEED)
            elif self.dx < 0:
                animate(self, PLAYER_JUMP_LEFT_IMAGES, PLAYER_JUMP_SPEED)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))