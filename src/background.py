import pygame
import random

from .particle_system import Partical_System
from .settings import WIDTH

class Background():
    def __init__(self, particle_image: pygame.Surface) -> None:
        self.particle_system = Partical_System(particle_image)
        self.max_particles = 100

    def create_particles(self):
        x = random.randint(0, WIDTH)
        y = 0
        dx = 0
        timer = random.randint(1, 50)
        gravity = 0
        dy = 8
        timer_speed = 0.1
        self.particle_system.create_particles(x, y, dx, dy, timer, gravity, timer_speed)
    
    def move_particles(self):
        self.particle_system.move_particles()
    
    def draw_particles(self, screen: pygame.Surface):
        self.particle_system.draw_particles(screen)
    
    def update_particles(self, screen: pygame.Surface):
        if len(self.particle_system.particle_group) <= self.max_particles:
            self.create_particles()
        self.move_particles()
        self.draw_particles(screen)