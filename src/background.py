import pygame
from pygame.locals import *
import random

from .particle_system import Partical_System
from .settings import WIDTH, HEIGHT, BACKGROUND_MOON_IMAGE

class Background():
    def __init__(self, particle_image: pygame.Surface) -> None:
        self.particle_system = Partical_System(particle_image)
        self.max_particles = 100
        self.moon_img = BACKGROUND_MOON_IMAGE

    def create_particles(self) -> None:
        x = random.randint(0, WIDTH)
        y = 0
        dx = 0
        timer = random.randint(1, 50)
        gravity = 0
        dy = 8
        timer_speed = 0.1
        self.particle_system.create_particles(x, y, dx, dy, timer, gravity, timer_speed)
    
    def move_particles(self) -> None:
        self.particle_system.move_particles()
    
    def draw_particles(self, screen: pygame.Surface) -> None:
        self.particle_system.draw_particles(screen)
    
    def destroy_particles(self) -> None:
        for particle in self.particle_system.particle_group.sprites():
            if particle.rect.y >= HEIGHT:
                self.particle_system.particle_group.remove(particle)

    def update_particles(self, screen: pygame.Surface) -> None:
        if len(self.particle_system.particle_group) <= self.max_particles:
            self.create_particles()
        self.move_particles()
        self.draw_particles(screen)
        screen.blit(self.moon_img, (1000, 100))