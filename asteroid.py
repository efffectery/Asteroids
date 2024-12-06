from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        ran_angle = random.uniform(20, 50)

        new_ast1_vel = self.velocity.rotate(ran_angle)
        new_ast2_vel = self.velocity.rotate(-ran_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast1.velocity = new_ast1_vel * 1.2

        new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast2.velocity = new_ast2_vel * 1.2




