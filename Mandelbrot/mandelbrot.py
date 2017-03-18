import math, pygame, colorsys
from Complex import Complex
from Text import Text

xcen = 0
zoom = 2 # Total width /2
zoomfactor = 2 #Amount to zoom in by
ycen = 0
n = 40

def mapvalue(value,normalmin,normalmax,scalemin,scalemax):
    deltascale = scalemax - scalemin
    deltanormal = normalmax - normalmin
    ratio = value / deltanormal
    return scalemin + deltascale * ratio


def diverge(c,maxn):
    z = Complex(0,0)
    n = 0
    while n < maxn:
        z = z.squared() + c
        if z.modulus() > 16:
            return n
        n += 1

    return n

def draw(screen_width,screen_height,xcen,ycen,zoom,screen,maxn):
    for x in range(1,screen_width):
        for y in range(1,screen_height):
            c = Complex(mapvalue(x,0,screen_width,xcen - zoom,xcen + zoom),mapvalue(y,0,screen_height,ycen - zoom,ycen + zoom))
            n = diverge(c,maxn)
            brightness = mapvalue(n,0,maxn,1,0)
            try:
                rgb = colorsys.hls_to_rgb(brightness,0.5, 1) #values need multiplying by 255
                screen.fill((rgb[0] * 255,rgb[1] * 255,rgb[2] * 255), ([x,y], (1, 1)))
            except:
                print("Could not paint pixel")

def updatetext(screen,postext,title):
    screen.fill(BLACK,([0,0],[max(title.width(),postext.width())+1,1 + postext.height() * 2]))
    title.render(screen)
    postext.render(screen)


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,51,51)

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

draw(screen_width,screen_height,xcen,ycen,zoom,screen,n)

title.text = "Mandelbrot Set | Zoom: " + str(1/zoom)
title.render(screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            n = int(input("Enter a new value of n: "))
            title.text = "Mandelbrot Set | Zoom: " + str(1/zoom)
            postext.text = "Generating new set.."
            updatetext(screen,postext,title)
            pygame.display.flip()
            draw(screen_width,screen_height,xcen,ycen,zoom,screen,n)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            zoomfactor = int(input("Enter a new zoomfactor (currently " + str(zoomfactor) + "): "))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            xcen = mapvalue(pos[0],0,screen_width,xcen - zoom,xcen + zoom)
            ycen = mapvalue(pos[1],0,screen_height,ycen - zoom,ycen + zoom)
            zoom = zoom / zoomfactor
            title.text = "Mandelbrot Set | Zoom: " + str(1/zoom)
            postext.text = "Generating new set.."
            updatetext(screen,postext,title)
            pygame.display.flip()
            draw(screen_width,screen_height,xcen,ycen,zoom,screen,n)


    pos = pygame.mouse.get_pos()
    postext.text = "X:" + str(pos[0]) + " Y:" + str(pos[1])
    updatetext(screen,postext,title)
    clock.tick(30)
    pygame.display.flip()

pygame.quit()
