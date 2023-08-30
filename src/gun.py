import pygame
import math
import random
from copy import deepcopy

from .functions import compute_angle, rotate
from .bullet import Bullet
from .particle_system import Partical_System
from .settings import *

class Simple_Gun(pygame.sprite.Sprite):
    '''
    Simple Gun which shoots bullets.
    '''
    def __init__(self, obj) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.obj = obj # Object with which it is attached.
        self.image = SIMPLE_GUN_IMAGE
        self.rect = self.image.get_rect()
        self.angle = 0

        # Bullet Variables.
        self.bullet_img = SIMPLE_GUN_BULLET_IMAGE
        self.bullet_group = pygame.sprite.Group()
        self.bullet_damage = SIMPLE_GUN_BULLET_DAMAGE
        self.bullet_speed = SIMPLE_GUN_BULLET_SPEED
        self.bullet_timer = SIMPLE_GUN_BULLET_TIMER # The original value.
        self.bullet_timer_copy = deepcopy(self.bullet_timer)
        
        # Partical System.
        self.is_particle_system = False
        self.particle_system = Partical_System(SIMPLE_GUN_PARTICLE_IMAGE)

    def rotate_gun(self, coords) -> None:
        x, y = (self.obj.rect.x + (self.obj.rect.width/2), self.obj.rect.y + (self.obj.rect.height/2))
        self.angle = compute_angle(((self.obj.rect.x, self.obj.rect.y)), coords)

        if self.angle > 90 or self.angle < -90:
            self.rotated_image, self.rotated_rect = rotate(self.image, -self.angle, (x, y))
            self.rotated_image = pygame.transform.flip(self.rotated_image, False, True)
        else:
            self.rotated_image, self.rotated_rect = rotate(self.image, self.angle, (x, y))

    def create_bullet(self, coords) -> None:
        self.bullet_timer_copy = self.bullet_timer
        bullet = Bullet(self.bullet_img)
        
        bullet.damage = self.bullet_damage
        bullet.speed = self.bullet_speed
        
        bullet.rect.x = self.rotated_rect.x
        bullet.rect.y = self.rotated_rect.y
      
        angle = compute_angle(coords, (bullet.rect.x, bullet.rect.y))
        x = math.cos(angle*(math.pi/180))*(180/math.pi)
        y = math.sin(angle*(math.pi/180))*(180/math.pi)
        bullet.x_vel = -x # IDK why putting '-' sign works here!
        bullet.y_vel = y

        self.bullet_group.add(bullet)
        
    def shoot_bullet(self) -> None:
        for bullet in self.bullet_group:
            bullet.move(self.bullet_speed)
        self.bullet_timer_copy -= 0.1
    
    def destroy_bullet(self, tile_group) -> None:
        if isinstance(tile_group, pygame.sprite.Group):
            hits = pygame.sprite.groupcollide(self.bullet_group, tile_group, True, False)
            if hits:
                for bullet, tile in hits.items():
                    self.is_particle_system = True
                    self.particle_system.create_particles(bullet.rect.x,
                                                        bullet.rect.y,
                                                        round(random.uniform(-1,1), 2)*10,
                                                        SIMPLE_GUN_PARTICLE_UPFORCE,
                                                        random.randint(1, 10),
                                                        SIMPLE_GUN_PARTICLE_GRAVITY,
                                                        SIMPLE_GUN_PARTICLE_TIMERSPEED)
        else:
            hits = pygame.sprite.spritecollide(tile_group, self.bullet_group, True, False)
            for bullet in hits:
                self.is_particle_system = True
                self.particle_system.create_particles(bullet.rect.x,
                                                    bullet.rect.y,
                                                    round(random.uniform(-1,1), 2)*10,
                                                    SIMPLE_GUN_PARTICLE_UPFORCE,
                                                    random.randint(1, 10),
                                                    SIMPLE_GUN_PARTICLE_GRAVITY,
                                                    SIMPLE_GUN_PARTICLE_TIMERSPEED)

    def draw(self, screen: pygame.Surface) -> None:
        self.bullet_group.draw(screen)
        screen.blit(self.rotated_image, self.rotated_rect)
        if self.is_particle_system:
            self.particle_system.update_particles(screen)