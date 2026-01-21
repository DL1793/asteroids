import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        degrees = random.uniform(20,50)
        angle1 = self.velocity.rotate(degrees)
        angle2 = self.velocity.rotate(-degrees)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(*self.position, new_radius)
        asteroid2 = Asteroid(*self.position, new_radius)
        asteroid1.velocity = angle1
        asteroid2.velocity = angle2