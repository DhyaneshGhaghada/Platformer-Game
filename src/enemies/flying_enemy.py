import pygame
import random
import math

from ..settings import *
from ..functions import animate, compute_angle
from ..weapons.gun import Simple_Gun
from ..particle_system import Partical_System

class FlyingEnemy(pygame.sprite.Sprite):
    def __init__(self, player) -> None:
        super().__init__()
        self.image = FLYING_ENEMY_ANIMATION['idle_right'][0][0]
        self.rect = self.image.get_rect()
        self.target_x, self.target_y = 0, 0
        self.move_timer = 10
        self.stay_timer = 10 # Enemy resting timer.
        self.current_sprite = 0
        self.movement_speed = 0.1
        self.dx, self.dy = 0,0
        self.player = player

        self.health = 5
        self.is_damage = False
        self.is_die = False
        
        self.gun = Simple_Gun(self)
        self.gun.particle_image = PLAYER_DAMAGE_PARTICLE_IMAGE
        self.gun.bullet_timer = 5
        self.gun.bullet_speed = 0.15

        # Damage Particle System.
        self.damage_particles = Partical_System(PLAYER_DAMAGE_PARTICLE_IMAGE)
        self.max_damage_particles = 10
        self.max_die_particles = 50

        # Enemy Spawn.
        self.spawn = True
        self.circle_radius = 0
        self.max_circle_radius = 50
        self.is_max_circle = False
        self.circle_width = 5

    def animation(self) -> None:
        direction_x = (self.player.rect.x - self.rect.x)
        if self.is_damage:
            self.health -= 1
            for _ in range(self.max_damage_particles):
                self.damage_particles.create_particles(x=self.rect.x + (self.rect.width/2),
                                                       y=self.rect.y + self.rect.height,
                                                       dx=round(random.uniform(-1,1), 2)*5,
                                                       dy=-2,
                                                       timer=random.randint(1, 10),
                                                       gravity=0.2,
                                                       timer_speed=0.1)
            if self.health <= 0:
                self.is_die = True
            if direction_x > 0:
                animate(self, FLYING_ENEMY_ANIMATION['damage_right'][0], FLYING_ENEMY_ANIMATION['damage_right'][1])
            elif direction_x < 0:
                animate(self, FLYING_ENEMY_ANIMATION['damage_left'][0], FLYING_ENEMY_ANIMATION['damage_left'][1])
        else:
            if direction_x > 0:
                animate(self, FLYING_ENEMY_ANIMATION['idle_right'][0], FLYING_ENEMY_ANIMATION['idle_right'][1])
            elif direction_x < 0:
                animate(self, FLYING_ENEMY_ANIMATION['idle_left'][0], FLYING_ENEMY_ANIMATION['idle_left'][1])

    def update(self, screen: pygame.Surface) -> None:
        # Enemy Spawn.
        if self.spawn:
            pygame.draw.circle(screen, (255, 255, 255), (self.rect.centerx, self.rect.centery), self.circle_radius, self.circle_width)
            if self.circle_radius <= self.max_circle_radius and self.is_max_circle == False:
                self.circle_radius += 1
            else:
                self.is_max_circle = True
            if self.is_max_circle:
                self.circle_radius -= 2
            if self.circle_radius < 0:
                self.is_max_circle = False
                self.spawn = False

        self.animation()

        self.rect.x += -self.dx*self.movement_speed
        self.rect.y += self.dy*self.movement_speed

        self.gun.rotate_gun((self.player.rect.x, self.player.rect.y))
        if self.gun.bullet_timer_copy <= 0:
            self.gun.create_bullet((self.player.rect.x+self.player.rect.width/2, self.player.rect.y+self.player.rect.height/2))
        self.gun.shoot_bullet()
        hits = self.gun.destroy_bullet(self.player)
        if hits:
            for _ in range(len(hits)):
                self.player.is_damage = True
        self.is_damage = False

        self.damage_particles.update_particles(screen)


class FlyingEnemySystem:
    def __init__(self, player, game_manager) -> None:
        self.game_manager = game_manager
        
        self.flying_enemy_group = pygame.sprite.Group()
        self.no_of_enemies = 5
        self.player = player

        self.death_particles = Partical_System(PLAYER_DAMAGE_PARTICLE_IMAGE)
        self.death_particles_max = 50
    
    def create_enemy(self):
        SFX['spawn'].play()
        enemy = FlyingEnemy(self.player)
        
        enemy.rect.x = random.randint(0, WIDTH)
        enemy.rect.y = random.randint(0, HEIGHT)
        
        enemy.target_x = random.randint(0, WIDTH)
        enemy.target_y = random.randint(0, HEIGHT)

        angle = compute_angle((enemy.target_x, enemy.target_y), (enemy.rect.x, enemy.rect.y))
        enemy.dx = math.cos(angle*(math.pi/180))*(180/math.pi)
        enemy.dy = math.sin(angle*(math.pi/180))*(180/math.pi)

        self.flying_enemy_group.add(enemy)
    
    def kill_enemy(self, screen:pygame.Surface):
        for enemy in self.flying_enemy_group.sprites():
            if enemy.is_die == True:
                SFX['blast'].play()
                self.game_manager.is_screenshake = True
                for _ in range(self.death_particles_max):
                    self.death_particles.create_particles(x=enemy.rect.x + (enemy.rect.width/2),
                                                          y=enemy.rect.y + enemy.rect.height,
                                                          dx=round(random.uniform(-1,1), 2)*10,
                                                          dy=-round(random.uniform(-1,1), 2)*10,
                                                          timer=random.randint(1, 10),
                                                          gravity=0.2,
                                                          timer_speed=0.1)
                enemy.kill()
                self.player.gain_health(gain_value=1)
                self.player.score += 1

        self.death_particles.update_particles(screen)

    def update_enemy(self, screen: pygame.Surface) -> None:
        self.kill_enemy(screen)

        if len(self.flying_enemy_group) <= self.no_of_enemies-1:
            self.create_enemy()

        self.flying_enemy_group.draw(screen)
        for enemy in self.flying_enemy_group.sprites():
            enemy.update(screen)
            enemy.move_timer -= 0.1

            is_left = enemy.rect.x < 0
            is_right = enemy.rect.x + enemy.rect.width > WIDTH
            is_up = enemy.rect.y < 0
            is_down = enemy.rect.y + enemy.rect.height > HEIGHT
            
            if enemy.move_timer <= 0 or is_left or is_right or is_down or is_up:
                enemy.dx = 0
                enemy.dy = 0
                enemy.stay_timer -= 0.1
                if enemy.stay_timer <= 0:
                    enemy.target_x = random.randint(0, WIDTH)
                    enemy.target_y = random.randint(0, HEIGHT)
                    angle = compute_angle((enemy.target_x, enemy.target_y), (enemy.rect.x, enemy.rect.y))
                    enemy.dx = math.cos(angle*(math.pi/180))*(180/math.pi)
                    enemy.dy = math.sin(angle*(math.pi/180))*(180/math.pi)
                    enemy.stay_timer = 10
                    enemy.move_timer = 10
        
            enemy.gun.draw(screen)