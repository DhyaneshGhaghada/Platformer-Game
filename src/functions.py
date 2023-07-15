import pygame
import math
import os
from typing import Tuple

def generate_pygame_image(dir: str, resize: tuple[int, int], is_reverse: bool) -> list[pygame.Surface]:
    '''
    This function generates pygame images based on the dir provided.
    '''
    image_list = []
    image_files = os.listdir(dir)
    for image_path in image_files:
        image = pygame.image.load(dir+'/'+image_path)
        image = pygame.transform.scale(image, resize)
        image = pygame.transform.flip(image, is_reverse, False)
        image_list.append(image)
    return image_list

def animate(obj, images: list[pygame.Surface], time: float) -> None:
    '''
    Animates the pygame.Surface type.
    '''
    obj.current_sprite += time
    if obj.current_sprite >= len(images):
        obj.current_sprite = 0
    obj.image = images[int(obj.current_sprite)]

def key_handler() -> dict:
    '''
    Key Handler for Player Movement.
    '''
    keys_dict = {
        'UP' : False,
        'RIGHT' : False,
        'LEFT' : False
    }
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        keys_dict['UP'] = True
    if keys[pygame.K_a]:
        keys_dict['LEFT'] = True
    if keys[pygame.K_d]:
        keys_dict['RIGHT'] = True
    
    return keys_dict

def collision_handler(obj, tiles: pygame.sprite.Group, direction: str) -> dict:
    '''
    Handles Collisions between a sprite and a group of sprites.
    '''

    # is_collision = pygame.sprite.spritecollide(obj, tiles, False)
    if direction == 'X':
        collision_dict = {
            'RIGHT' : False,
            'LEFT' : False
        }
        for sprite in tiles.sprites():
            if sprite.rect.colliderect(obj.rect):
                if obj.dx > 0:
                    obj.rect.right = sprite.rect.left
                    collision_dict['LEFT'] = True
                if obj.dx < 0:
                    obj.rect.left = sprite.rect.right
                    collision_dict['RIGHT'] = True

    if direction == 'Y':
        collision_dict = {
            'UP' : False,
            'DOWN' : False,
        }
        for sprite in tiles.sprites():
            if sprite.rect.colliderect(obj.rect):
                if obj.dy > 0:
                    obj.rect.bottom = sprite.rect.top
                    obj.dy = 0
                    collision_dict['DOWN'] = True
                if obj.dy < 0:
                    obj.rect.top = sprite.rect.bottom
                    collision_dict['UP'] = True

    return collision_dict

def compute_angle(point_a: Tuple[float, float], point_b: Tuple[float, float]) -> float:
    radian_value = math.atan2(point_b[1] - point_a[1], point_b[0] - point_a[0])
    degrees_value = (-radian_value)*(180/math.pi)
    return degrees_value

def rotate(surface, angle: float, coords: Tuple[float, float]) -> Tuple[pygame.Surface, pygame.Rect]:
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=coords)
    return (rotated_surface, rotated_rect)

def normalize(x: float, y: float) -> Tuple[float, float]:
    pythagorean_theorem = math.sqrt((x**2) + (y**2))
    x = x/pythagorean_theorem
    y = y/pythagorean_theorem
    return (x, y)