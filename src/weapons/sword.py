import pygame

from src.settings import *
from src.functions import rotate, compute_angle

class Sword(pygame.sprite.Sprite):
    def __init__(self, obj) -> None:
        super().__init__()
        self.obj = obj # Object with which sword is attached.
        self.image = SWORD_IMAGE
        self.rect = self.image.get_rect()
        self.img_offset = (5, 5)

    def rotate_sword(self, coords):
        x, y = (self.obj.rect.x + (self.obj.rect.width/2+self.img_offset[0]), self.obj.rect.y + (self.obj.rect.height/2+self.img_offset[1]))
        self.angle = compute_angle(((x, y)), coords)
        self.rotated_image, self.rotated_rect = rotate(self.image, self.angle, (x, y))
    
    def slash(self):
        pass

    def move_sword(self):
        self.rect.x, self.rect.y = self.obj.rect.x + (self.obj.rect.width/2+self.img_offset[0]), self.obj.rect.y + (self.obj.rect.height/2+self.img_offset[1])

    def update(self):
        self.rotate_sword(pygame.mouse.get_pos())
        self.move_sword()
    
    def draw(self, screen):
        screen.blit(self.rotated_image, self.rotated_rect)