import math, pygame
from Complex import Complex
from Text import Text

xcen = 0
xzoom = 2 # Total width /2
ycen = 0
yzoom = xzoom #Keeps scaling nice
def mapvalue(value,normalmin,normalmax,scalemin,scalemax):
    deltascale = scalemax - scalemin
    deltanormal = normalmax - normalmin
    ratio = value / deltanormal
    return scalemin + deltascale * ratio


def diverge(c):
    z = Complex(0,0)
    n = 0
    while n < 100:
        z = z.squared() + c
        if z.modulus() > 16:
            break
        n += 1

    return n

WHITE = (255,255,255)
BLACK = (0,0,0)

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Mandelbrot")

title = Text([1,1],WHITE)
title.text = "Mandelbrot Set Generator - D.Trickey"
title.render(screen)

postext = Text([1,1 + title.height()],WHITE)
postext.text = "Generating Set.."
postext.render(screen)

pygame.display.flip()

clock = pygame.time.Clock()
done = False

for x in range(1,screen_width):
    for y in range(1,screen_height):
        c = Complex(mapvalue(x,0,screen_width,xcen - xzoom,xcen + xzoom),mapvalue(y,0,screen_height,ycen - yzoom,ycen + yzoom))
        n = diverge(c)
        brightness = mapvalue(n,0,100,0,255)
        screen.fill((brightness,brightness,brightness), ([x,y], (1, 1)))

title.text = "Mandelbrot Set"
title.render(screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    pos = pygame.mouse.get_pos()
    postext.text = "X:" + str(pos[0]) + " Y:" + str(pos[1])
    screen.fill(BLACK,([0,0],[max(title.width(),postext.width())+1,1 + postext.height() * 2]))
    title.render(screen)
    postext.render(screen)
    clock.tick(30)
    pygame.display.flip()

pygame.quit()
