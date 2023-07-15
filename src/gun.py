import pygame
import math

from .functions import compute_angle, rotate
from .bullet import Bullet

class Simple_Gun(pygame.sprite.Sprite):
    '''
    Simple Gun which shoots bullets.
    Make Sure to fill these attr manually, 
    ' self.bullet_damage, self.bullet_speed, self.max_bullet '
    '''
    def __init__(self, player, gun_img: pygame.Surface, bullet_img: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = gun_img
        self.rect = self.image.get_rect()
        self.angle = 0

        # Bullet Variables.
        self.bullet_img = bullet_img
        self.bullet_group = pygame.sprite.Group()
        self.bullet_damage = 0
        self.bullet_speed = 0

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
        bullet = Bullet(self.bullet_img)
        
        bullet.damage = self.bullet_damage
        bullet.speed = self.bullet_speed
        
        bullet.rect.x = self.rotated_rect.x
        bullet.rect.y = self.rotated_rect.y

        # Computing Bullet's dx, dy.
        mx, my = pygame.mouse.get_pos()        
        angle = compute_angle((mx, my), (bullet.rect.x, bullet.rect.y))
        x = math.cos(angle*(math.pi/180))*(180/math.pi)
        y = math.sin(angle*(math.pi/180))*(180/math.pi)
        bullet.x_vel = -x # IDK why putting '-' sign works here perfectly!
        bullet.y_vel = y

        self.bullet_group.add(bullet)
        
    def shoot_bullet(self) -> None:
        for bullet in self.bullet_group:
            bullet.move(self.bullet_speed)
    
    def destroy_bullet(self, tile_group: pygame.sprite.Group) -> None:
        hits = pygame.sprite.groupcollide(self.bullet_group, tile_group, True, False)

    def update_bullet_status(self, tile_group: pygame.sprite.Group) -> None:
        if pygame.mouse.get_pressed()[0] and len(self.bullet_group) == 0:
            self.create_bullet()
        self.shoot_bullet()
        self.destroy_bullet(tile_group)

    def draw(self, screen: pygame.Surface) -> None:
        self.bullet_group.draw(screen)
        screen.blit(self.rotated_image, self.rotated_rect)