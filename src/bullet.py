import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.damage = 0 # The damage Applied on the enemy.
        self.speed = 0 # the speed of the bullet.

    def move(self, x, y) -> None:
        self.rect.x += x*self.speed
        self.rect.y += y*self.speed