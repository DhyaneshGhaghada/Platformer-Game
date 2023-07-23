import pygame

class Particle(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()

        self.timer = 0
        self.dx, self.dy = 0, 0