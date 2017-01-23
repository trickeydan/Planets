from noise import pnoise2, snoise2
import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,51,51)

def draw(screen_width,screen_height,screen,zoom):
    scale = 1/zoom
    for x in range(1,screen_width):
        for y in range(1,screen_height):
            value = 128 + (snoise2(x * scale,y * scale) * 127)
            screen.fill((value,value,value), ([x,y], (1, 1)))

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Perlin2D")

clock = pygame.time.Clock()
done = False
zoom = 1
zoomchange = 1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    draw(screen_width,screen_height,screen,zoom)
    zoom += zoomchange
    if zoom >= 22 or zoom == 1:
        zoomchange *= -1
    clock.tick(30)
    pygame.display.flip()

pygame.quit()
