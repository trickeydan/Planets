import pygame
import random
from Planet import Planet
from Vector import Vector
from Text import Text

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

# Create a sun.
sun = Planet(WHITE,20,Vector(screen_width/2,screen_height/2),Vector(0,0),True)
sprites.add(sun)

planets = pygame.sprite.Group()

satellite = Planet(GREEN,10,Vector(screen_width/4,screen_height/4),Vector(2,-1),False)
sprites.add(satellite)
planets.add(satellite)

satellite2 = Planet(RED,12,Vector(3 * screen_width/4,3 * screen_height/4),Vector(2,-1),False)
sprites.add(satellite2)
planets.add(satellite2)

planetcount = Text([1,1],WHITE)
gpdisplay = Text([1,1 + planetcount.height()],WHITE)
kedisplay = Text([1,1 + (planetcount.height() * 2)],WHITE)
edisplay = Text([1,1 + (planetcount.height() * 3)],WHITE)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    sprites.update(sprites)
    planets_hit = pygame.sprite.spritecollide(sun,planets, True)
    GPE = 0
    KE = 0
    for obj in planets:
        GPE += obj.gEnergy(sun)
        KE += obj.kEnergy()

    planetcount.text = "Planet Count: " + str(len(planets))
    gpdisplay.text = "GPE: " + "{0:.2f}".format(GPE)
    kedisplay.text = "KE: " + "{0:.2f}".format(KE)
    edisplay.text = "Total E: " + "{0:.2f}".format(GPE+KE)

    screen.fill(BLACK)
    sprites.draw(screen)
    for obj in sprites:
        obj.velocity.draw(screen,obj.centPos())

    planetcount.render(screen)
    gpdisplay.render(screen)
    kedisplay.render(screen)
    edisplay.render(screen)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
