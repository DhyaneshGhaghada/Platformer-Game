import pygame

class Textbox:
    def __init__(self, font_name, font_size) -> None:
        self.font = pygame.font.Font(font_name, font_size)
        self.texts = []
    
    def create_text(self, text, color, coords) -> None:
        text = self.font.render(text, False, color)
        self.texts.append([text, coords])
    
    def clear_text(self) -> None:
        self.texts = []
    
    def draw_text(self, screen) -> None:
        for text,coords in self.texts:
            screen.blit(text, coords)