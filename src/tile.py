import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface) -> None:
        # Calling Parent Class's Constructor.
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.rect = self.image.get_rect()