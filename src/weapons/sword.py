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
        self.angle = 0

        # Slash
        self.is_slash = False
        self.slash_rotation_power = -20

    def rotate_sword(self, coords):
        x, y = (self.obj.rect.x + (self.obj.rect.width/2+self.img_offset[0]), self.obj.rect.y + (self.obj.rect.height/2+self.img_offset[1]))
        if self.is_slash != True:
            self.angle = compute_angle(((x, y)), coords)
            self.rotated_image, self.rotated_rect = rotate(self.image, self.angle, (x, y))
        else:
            self.angle += self.slash_rotation_power
            self.rotated_image, self.rotated_rect = rotate(self.image, self.angle, (x, y))

    def slash(self):
        self.is_slash = True

    def move_sword(self):
        self.rect.x, self.rect.y = self.obj.rect.x + (self.obj.rect.width/2+self.img_offset[0]), self.obj.rect.y + (self.obj.rect.height/2+self.img_offset[1])

    def update(self):
        self.rotate_sword(pygame.mouse.get_pos())
        self.move_sword()
        self.is_slash = False
    
    def draw(self, screen):
        screen.blit(self.rotated_image, self.rotated_rect)