import pygame

from .tile import Tile

class Tilemap:
    def __init__(self, map_data: list[list], tile_size: int, tiles: list) -> None:
        self.tiles_group = pygame.sprite.Group()

        for i in range(len(map_data)):
            for j in range(len(map_data[0])):
                if map_data[i][j] == 1:
                    tile = Tile(tiles[0])
                    tile.rect.x = j*tile_size
                    tile.rect.y = i*tile_size
                    self.tiles_group.add(tile)
    
    def draw(self, screen: pygame.Surface) -> None:
        self.tiles_group.draw(screen)
        