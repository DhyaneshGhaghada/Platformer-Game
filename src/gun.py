from typing import Any
import pygame

from .settings import SIMPLE_GUN_BULLET_IMAGE, SIMPLE_GUN_IMAGE, SIMPLE_GUN_BULLET_DAMAGE, SIMPLE_GUN_BULLET_SPEED, SIMPLE_GUN_MAX_BULLET_SHOOT
from .functions import compute_angle, rotate, normalize
from .bullet import Bullet

class Simple_Gun(pygame.sprite.Sprite):
    def __init__(self, player) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = SIMPLE_GUN_IMAGE
        self.rect = self.image.get_rect()
        self.angle = 0

        # Bullet Variables.
        self.bullet_group = pygame.sprite.Group()
        self.bullet_damage = SIMPLE_GUN_BULLET_DAMAGE
        self.bullet_speed = SIMPLE_GUN_BULLET_SPEED
        self.max_bullet_shoot = SIMPLE_GUN_MAX_BULLET_SHOOT

    def rotate_gun_on_mouse_pos(self) -> None:
        mx, my = pygame.mouse.get_pos()
        x, y = (self.player.rect.x + (self.player.rect.width/2), self.player.rect.y + (self.player.rect.height/2))
        self.angle = compute_angle(((self.player.rect.x, self.player.rect.y)), (mx, my))

        if self.angle > 90 or self.angle < -90:
            self.rotated_image, self.rotated_rect = rotate(self.image, -self.angle, (x, y))
            self.rotated_image = pygame.transform.flip(self.rotated_image, False, True)
        else:
            self.rotated_image, self.rotated_rect = rotate(self.image, self.angle, (x, y))

    def create_bullet(self) -> None:
        if len(self.bullet_group) <= self.max_bullet_shoot:
            bullet = Bullet(SIMPLE_GUN_BULLET_IMAGE)
            bullet.damage = self.bullet_damage
            bullet.speed = self.bullet_speed
            self.bullet_group.add(bullet)
        
    def shoot_bullet(self) -> None:
        for bullet in self.bullet_group:
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                x, y = normalize( mx - self.rect.x, my - self.rect.y )
                bullet.move(x, y)
    
    def destroy_bullet(self) -> None:
        pass

    def update_bullet_status(self) -> None:
        self.create_bullet()
        self.shoot_bullet()
        self.destroy_bullet()

    def draw(self, screen: pygame.Surface) -> None:
        self.bullet_group.draw(screen)
        screen.blit(self.rotated_image, self.rotated_rect)