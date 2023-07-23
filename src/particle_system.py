import pygame
import random

from .particle import Particle

class Partical_System:
    def __init__(self, image: pygame.Surface) -> None:
        self.particle_image = image
        self.particle_group = pygame.sprite.Group()


        # Make sure to add values to this variables manually.
        self.up_force = 0
        self.gravity = 0
        self.timer_speed = 0

    def create_particles(self, x, y) -> None:
        p = Particle(self.particle_image)
        p.rect.x, p.rect.y = x, y
        p.dx = random.randint(0, 40) / 10 - 1
        p.dy = self.up_force
        p.timer = random.randint(1, 10)
        self.particle_group.add(p)

    def move_particles(self) -> None:
        for particle in self.particle_group.sprites():
            particle.rect.x += particle.dx
            particle.rect.y += particle.dy
            particle.timer -= self.timer_speed

            # Gravity sort of!
            particle.dy += self.gravity

            if particle.timer <= 0:
                self.particle_group.remove(particle)

    def draw_particles(self, screen: pygame.Surface) -> None:
        self.particle_group.draw(screen)
    
    def update_particles(self, screen: pygame.Surface) -> None:
        self.move_particles()
        self.draw_particles(screen)