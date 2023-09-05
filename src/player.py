import pygame
import random

from .functions import collision_handler, key_handler, animate
from .settings import *
from .particle_system import Partical_System
from .gun import Simple_Gun

from src.UI_Lib.healthbar import HealthBar

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img: pygame.Surface, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.dx = 0
        self.dy = 0
        
        self.current_sprite = 0
        self.in_ground = False
        self.health = PLAYER_HEALTH
        self.score = 0 # Player's Score.

        self.is_kill = False
        self.is_damage = False
        self.is_kill = False # For the First Animation.
        self.is_kill_2 = False # For the Second Animation.

        # damage particle system.
        self.max_damage_particles = 10
        self.damage_particle_system = Partical_System(PLAYER_DAMAGE_PARTICLE_IMAGE)

        self.gun = Simple_Gun(self)
        
        self.health_bar = HealthBar(HEALTHBAR_IMAGE, (10, 10), self.health)

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
                SFX['jump'].play()
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
            animate(self, PLAYER_ANIMATION['die_2'][0], PLAYER_ANIMATION['die_2'][1])
        elif self.is_kill:
            animate(self, PLAYER_ANIMATION['die_1'][0], PLAYER_ANIMATION['die_1'][1])
            SFX['death'].play()
            if self.current_sprite >= len(PLAYER_ANIMATION['die_1'][0])-1:
                self.is_kill_2 = True
        elif self.is_damage:
            animate(self, PLAYER_ANIMATION['damage'][0], PLAYER_ANIMATION['damage'][1])
            self.health_bar.damage(damage_value=0.1)
            self.health -= 0.1 # Health Declining by one.
            for _ in range(self.max_damage_particles):
                self.damage_particle_system.create_particles(x=self.rect.x + (self.rect.width/2),
                                                            y=self.rect.y + self.rect.height,
                                                            dx=round(random.uniform(-1,1), 2)*5,
                                                            dy=-2,
                                                            timer=random.randint(1, 10),
                                                            gravity=0.2,
                                                            timer_speed=0.1)
        else:
            if direction == 'X' and self.in_ground == True:
                if self.dx > 0:
                    animate(self, PLAYER_ANIMATION['run_right'][0], PLAYER_ANIMATION['run_right'][1])
                elif self.dx < 0:
                    animate(self, PLAYER_ANIMATION['run_left'][0], PLAYER_ANIMATION['run_left'][1])
                else:
                    animate(self, PLAYER_ANIMATION['idle'][0], PLAYER_ANIMATION['idle'][1])
            elif direction == 'Y' and self.in_ground == False:
                if self.dx >= 0:
                    animate(self, PLAYER_ANIMATION['jump_right'][0], PLAYER_ANIMATION['jump_right'][1])
                elif self.dx < 0:
                    animate(self, PLAYER_ANIMATION['jump_left'][0], PLAYER_ANIMATION['jump_left'][1])

    def spike_collision(self, spikes_group: pygame.sprite.AbstractGroup) -> None:
        self.is_damage = False
        for spike in spikes_group.sprites():
            if spike.rect.colliderect(self.rect):
                self.is_damage = True
    
    def kill(self) -> None:
        if self.health <= 0:
            self.is_kill = True

    def gain_health(self, gain_value) -> None:
        if self.health + gain_value <= PLAYER_HEALTH:
            self.health += gain_value
            self.health_bar.gain(gain_value=gain_value)

    def update(self,
               tiles: pygame.sprite.AbstractGroup,
               spikes_group: pygame.sprite.AbstractGroup) -> None:
        self.kill()
        self.movement(tiles)
        self.spike_collision(spikes_group)

        # Gun Stuff.
        self.gun.rotate_gun(pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[0] and self.gun.bullet_timer_copy <= 0:
            self.gun.create_bullet(pygame.mouse.get_pos())
        self.gun.shoot_bullet()
        self.gun.destroy_bullet(tiles)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.damage_particle_system.update_particles(screen)
        self.gun.draw(screen)
        self.health_bar.draw(screen)

    def enemy_damage(self, enemy) -> None:
        hits = self.gun.destroy_bullet(enemy)
        if hits:
            for bullet, enemy in hits.items():
                enemy[0].is_damage = True