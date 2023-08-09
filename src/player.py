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
        self.health = PLAYER_HEALTH
        self.is_kill = False
        self.is_damage = False
        self.is_kill = False # For the First Anime.
        self.is_kill_2 = False # For the Second Anime.

    def movement(self, tiles: pygame.sprite.AbstractGroup) -> None:
        keys = key_handler()

        if self.is_kill != True:
            # Horizontal Movement.
            if keys['LEFT']:
                self.dx += -PLAYER_HORIZONTAL_SPEED
            elif keys['RIGHT']:
                self.dx += PLAYER_HORIZONTAL_SPEED

        self.rect.x += self.dx
        self.collisionX = collision_handler(self, tiles, 'X')
        self.animation('X')
        self.dx = 0

        if self.is_kill != True:
            # Vertical Movement.
            if keys['UP'] and self.in_ground == True:
                self.dy = PLAYER_JUMP_FORCE
                self.in_ground = False
            self.dy += GRAVITY
        else:
            if self.is_kill_2 == True:
                self.dy = -3 # Player Going To Heaven.

        self.rect.y += self.dy
        if self.is_kill != True:
            self.collisionY = collision_handler(self, tiles, 'Y')
        self.animation('Y')
        if self.collisionY['DOWN']:
            self.in_ground = True

    def animation(self, direction: str) -> None:
        if self.is_kill_2:
            animate(self, PLAYER_DIE_2_IMAGE, PLAYER_DIE_2_TIME)
        elif self.is_kill:
            animate(self, PLAYER_DIE_1_IMAGE, PLAYER_DIE_1_TIME)
            if self.current_sprite >= len(PLAYER_DIE_1_IMAGE)-1:
                self.is_kill_2 = True
        elif self.is_damage:
            animate(self, PLAYER_DAMAGE_IMAGE, PLAYER_DAMAGE_TIME)
        else:
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

    def spike_collision(self, spikes_group: pygame.sprite.AbstractGroup) -> None:
        self.is_damage = False
        for spike in spikes_group.sprites():
            if spike.rect.colliderect(self.rect):
                self.health -= 0.1
                self.is_damage = True
    
    def kill(self) -> None:
        if self.health <= 0:
            self.is_kill = True

    def update(self,
               tiles: pygame.sprite.AbstractGroup,
               spikes_group: pygame.sprite.AbstractGroup) -> None:
        self.kill()
        self.movement(tiles)
        self.spike_collision(spikes_group)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))