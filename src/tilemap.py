import pygame
from pygame.sprite import AbstractGroup

class Tile(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface) -> None:
        # Calling Parent Class's Constructor.
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.rect = self.image.get_rect()
    
    def __repr__(self) -> str:
        return f'<class Tile> X: {self.rect.x} Y: {self.rect.y} W: {self.rect.width} H: {self.rect.height}'

class Spike(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface) -> None:
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

    def __repr__(self) -> str:
        return f'<class Spike> X: {self.rect.x} Y: {self.rect.y} W: {self.rect.width} H: {self.rect.height}'

class Tilemap:
    def __init__(self, map_data: list[list], tile_size: int, tiles: list) -> None:
        self.tiles_group = pygame.sprite.Group()
        self.spikes_group = pygame.sprite.Group()
        
        for i in range(len(map_data)):
            for j in range(len(map_data[0])):
                if map_data[i][j] == 1:
                    tile = Tile(tiles[0])
                    tile.rect.x = j*tile_size
                    tile.rect.y = i*tile_size
                    self.tiles_group.add(tile)
                if map_data[i][j] == 2:
                    tile = Spike(tiles[1])
                    tile.rect.x = j*tile_size
                    tile.rect.y = i*tile_size+(tile_size-10) # Since tiles of size 32 are to be subtracted with spikes height to get properly aligned.
                    self.spikes_group.add(tile)

    def draw(self, screen: pygame.Surface) -> None:
        self.spikes_group.draw(screen)
        self.tiles_group.draw(screen)