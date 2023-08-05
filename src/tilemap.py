import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface) -> None:
        # Calling Parent Class's Constructor.
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.rect = self.image.get_rect()

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
                if map_data[i][j] == 2:
                    tile = Tile(tiles[1])
                    tile.rect.x = j*tile_size
                    tile.rect.y = i*tile_size+(tile_size-10) # Since tiles of size 32 are to be subtracted with spikes height to get properly aligned.
                    self.tiles_group.add(tile)
    
    def draw(self, screen: pygame.Surface) -> None:
        self.tiles_group.draw(screen)