import pygame
from Vector import Vector

class Planet(pygame.sprite.Sprite):

    G = 0.3

    def __init__(self, colour,mass,pos,velocity,fixed):
        self.radius = int(0.05 * mass * mass)
        self.velocity = velocity
        self.fixed = fixed
        self.mass = mass
        self.pos = pos

        super().__init__()

        self.image = pygame.Surface([self.radius * 2, self.radius * 2])

        pygame.draw.circle(self.image,colour,[self.radius,self.radius],self.radius)

        self.rect = self.image.get_rect()

        self.goto(self.pos)

    def update(self,objects,sun):

        if not self.fixed:
            self.rect.y += 1

            totalforce = Vector([0,0])

            for obj in objects:
                if obj != self:
                    delta = self.pos - obj.pos
                    rsquared = delta.magnitude() ** 2
                    forcemag = Planet.G * obj.mass * self.mass / rsquared
                    forcevector = delta * forcemag
                    totalforce = totalforce + forcevector

            acc = totalforce.divide(self.mass)
            self.velocity = self.velocity - acc

            self.pos = self.pos + self.velocity
            self.goto(self.pos)

            if self.pos.subtract(sun.pos).magnitude() > 1500:
                self.kill()

    def centPos(self):
        return self.pos + Vector([self.radius /2,self.radius /2])

    def goto(self,pos):
        self.rect.x = pos.x - self.radius /2
        self.rect.y = pos.y - self.radius /2

    def kEnergy(self):
        return 0.5 * self.mass * self.velocity.magnitude() ** 2
    def gEnergy(self,sun):
        return Planet.G * self.mass * sun.mass / self.pos.subtract(sun.pos).magnitude()
