import pygame
class HealthBar:
    def __init__(self, img: pygame.Surface, coords, health: int) -> None:
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords
        self.health = self.rect.width/health
        self.blood_remain = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    def damage(self, damage_value) -> None:
        self.blood_remain.width -= self.health*damage_value
    
    def gain(self, gain_value) -> None:
        self.blood_remain.width += self.health*gain_value
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (255, 0, 0), self.blood_remain)
        screen.blit(self.image, self.rect)