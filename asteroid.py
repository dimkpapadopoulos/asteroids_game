import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            new_velocity = [self.velocity.rotate(angle), self.velocity.rotate(-angle)]

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x,y = self.position
            a1 = Asteroid(x,y,new_radius)
            a2 = Asteroid(x,y,new_radius)
            a1.velocity = new_velocity[0]*1.2
            a2.velocity = new_velocity[1]*1.2

    def update(self, dt):
        self.position += self.velocity * dt