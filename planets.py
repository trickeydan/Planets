import pygame
import random
from Planet import Planet
from Vector import Vector

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Planets Simulation")


sprites = pygame.sprite.Group()

# Create a stationary planet.
planet = Planet(WHITE,20,Vector(screen_width/2,screen_height/2),Vector(0,0),True)
sprites.add(planet)

satellite = Planet(GREEN,10,Vector(screen_width/4,screen_height/4),Vector(2,-1),False)
sprites.add(satellite)


done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    sprites.update(sprites)
    sprites.draw(screen)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
