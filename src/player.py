import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img: pygame.Surface, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.get_rect().x, self.image.get_rect().y = x, y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.dx = 0
        self.dy = 0
        self.current_sprite = 0
        self.mass = 1

    def apply_gravity(self, gravity: float) -> None:
        self.dy += gravity*self.mass

    def apply_jump() -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))