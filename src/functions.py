import pygame
import os

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
    if obj.current_sprite > len(images):
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

def collision_handler(obj, tiles, direction) -> dict:
    '''
    Handles Collisions between a sprite and a group of sprites.
    '''
    collision_dict = {
        'UP' : False,
        'DOWN' : False,
        'RIGHT' : False,
        'LEFT' : False
    }
    is_collision = pygame.sprite.spritecollide(obj, tiles, False)
    if direction == 'X' and is_collision:
        if obj.dx > 0:
            obj.rect.right = is_collision[0].rect.left
            collision_dict['LEFT'] = True
        if obj.dx < 0:
            obj.rect.left = is_collision[0].rect.right
            collision_dict['RIGHT'] = True
    if direction == 'Y' and is_collision:
        if obj.dy > 0:
            obj.rect.bottom = is_collision[0].rect.top
            collision_dict['DOWN'] = True
        if obj.dy < 0:
            obj.rect.bottom = is_collision[0].rect.top
            collision_dict['UP'] = True

    return (collision_dict, is_collision)