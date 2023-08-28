import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.damage = 0 # The damage Applied on the enemy.

        # Since we want to find coordinates only once when we create bullet.
        # We will keep that speed here and then add it in move move function to the bullet's rect.
        self.x_vel = 0
        self.y_vel = 0

    def move(self, bullet_speed: float) -> None:
        self.rect.x += self.x_vel*bullet_speed
        self.rect.y += self.y_vel*bullet_speed
