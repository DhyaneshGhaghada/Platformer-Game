import pygame

class Particle(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()

        self.timer = 0
        self.dx, self.dy = 0, 0
        self.gravity = 0
        self.timer_speed = 0

class Partical_System:
    def __init__(self, image: pygame.Surface) -> None:
        self.particle_image = image
        self.particle_group = pygame.sprite.Group()

    def create_particles(self, x, y, dx, dy, timer, gravity, timer_speed) -> None:
        p = Particle(self.particle_image)
        p.rect.x, p.rect.y = x, y
        p.dx = dx 
        p.dy = dy
        p.timer = timer
        p.gravity = gravity
        p.timer_speed = timer_speed
        self.particle_group.add(p)

    def move_particles(self) -> None:
        for particle in self.particle_group.sprites():
            particle.rect.x += particle.dx
            particle.rect.y += particle.dy
            particle.timer -= particle.timer_speed

            # Gravity sort of!
            particle.dy += particle.gravity

            if particle.timer <= 0:
                self.particle_group.remove(particle)

    def draw_particles(self, screen: pygame.Surface) -> None:
        self.particle_group.draw(screen)
    
    def update_particles(self, screen: pygame.Surface) -> None:
        self.move_particles()
        self.draw_particles(screen)