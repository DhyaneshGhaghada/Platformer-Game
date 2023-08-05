import pygame
import math
import random

from .functions import compute_angle, rotate
from .bullet import Bullet
from .particle_system import Partical_System

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
        self.BULLET_TIMER = 0 # The original value.
        self.bullet_timer_copy = 0 # The Value that gets changed.


        self.is_particle = False
    
    def create_particles(self, particle_img: pygame.Surface, up_force: float, gravity: float, timer_speed: float, max_particles: int) -> None:
        self.is_particle = True
        # Partical System.
        self.particle_system = Partical_System(particle_img)
        self.particle_system_up_force = up_force
        self.particle_system_gravity = gravity
        self.particle_system_timer_speed = timer_speed
        self.particle_system_max_particles = max_particles

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
        self.bullet_timer_copy = self.bullet_timer
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
        bullet.x_vel = -x # IDK why putting '-' sign works here!
        bullet.y_vel = y

        self.bullet_group.add(bullet)
        
    def shoot_bullet(self) -> None:
        for bullet in self.bullet_group:
            bullet.move(self.bullet_speed)
        self.bullet_timer_copy -= 0.1
    
    def destroy_bullet(self, tile_group: pygame.sprite.Group) -> None:
        hits = pygame.sprite.groupcollide(self.bullet_group, tile_group, True, False)
        if hits:
            for bullet, tile in hits.items():
                for _ in range(self.particle_system_max_particles):
                    self.particle_system.create_particles(bullet.rect.x, bullet.rect.y, round(random.uniform(-1,1), 2)*10, self.particle_system_up_force, random.randint(1, 10), self.particle_system_gravity, self.particle_system_timer_speed)

    def update_bullet_status(self, tile_group: pygame.sprite.Group) -> None:
        if pygame.mouse.get_pressed()[0] and self.bullet_timer_copy <= 0:
            self.bullet_timer_copy = self.BULLET_TIMER
            self.create_bullet()
        self.shoot_bullet()
        self.destroy_bullet(tile_group)

    def draw(self, screen: pygame.Surface) -> None:
        self.bullet_group.draw(screen)
        screen.blit(self.rotated_image, self.rotated_rect)
        self.particle_system.update_particles(screen)