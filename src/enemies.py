import pygame
import random
import math

from .settings import *
from .functions import animate, compute_angle
from .gun import Simple_Gun

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
        self.gun = Simple_Gun(self)
        self.gun.bullet_timer = 5
        self.gun.bullet_speed = 0.2

    def update(self, tiles) -> None:
        direction_x = (self.player.rect.x - self.rect.x)
        if direction_x > 0:
            animate(self, FLYING_ENEMY_ANIMATION['idle_right'][0], FLYING_ENEMY_ANIMATION['idle_right'][1])
        elif direction_x < 0:
            animate(self, FLYING_ENEMY_ANIMATION['idle_left'][0], FLYING_ENEMY_ANIMATION['idle_left'][1])

        self.rect.x += -self.dx*self.movement_speed
        self.rect.y += self.dy*self.movement_speed

        self.gun.rotate_gun((self.player.rect.x, self.player.rect.y))
        if self.gun.bullet_timer_copy <= 0:
            self.gun.create_bullet((self.player.rect.x, self.player.rect.y))
        self.gun.shoot_bullet()
        self.gun.destroy_bullet(self.player)
        self.gun.destroy_bullet(tiles)


class FlyingEnemySystem:
    def __init__(self, player, tiles) -> None:
        self.flying_enemy_group = pygame.sprite.Group()
        self.no_of_enemies = 5
        self.player = player
        self.tiles = tiles
    
    def create_enemy(self):
        enemy = FlyingEnemy(self.player)
        enemy.target_x = random.randint(0, WIDTH)
        enemy.target_y = random.randint(0, HEIGHT)

        angle = compute_angle((enemy.target_x, enemy.target_y), (enemy.rect.x, enemy.rect.y))
        enemy.dx = math.cos(angle*(math.pi/180))*(180/math.pi)
        enemy.dy = math.sin(angle*(math.pi/180))*(180/math.pi)

        self.flying_enemy_group.add(enemy)

    def update_enemy(self, screen: pygame.Surface) -> None:
        if len(self.flying_enemy_group) <= self.no_of_enemies-1:
            self.create_enemy()

        self.flying_enemy_group.draw(screen)
        for enemy in self.flying_enemy_group.sprites():
            enemy.update(self.tiles)
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