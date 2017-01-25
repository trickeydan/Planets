# Brick.py
# Trickeydan/PythonScience/BrickBreaker
# D.Trickey 2017
#
# Class file for Brick

import pygame
from random import randint

class Brick(pygame.sprite.Sprite):

    BLOCK_WIDTH = 40
    BLOCK_HEIGHT = 20
    X_AMOUNT = 12 # The width in blocks, not pixels
    Y_AMOUNT = 8 # The Height is the height in blocks, not pixels

    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.Surface([Brick.BLOCK_WIDTH,Brick.BLOCK_HEIGHT])

        self.image.fill((randint(0,255),randint(0,255),randint(0,255)))

        self.rect = self.image.get_rect()

        self.rect.x = Brick.BLOCK_WIDTH * (x + 2)
        self.rect.y = Brick.BLOCK_HEIGHT * (y + 2)

def generateBricks():

    bricks = pygame.sprite.Group()

    startpos = [Brick.BLOCK_WIDTH,Brick.BLOCK_HEIGHT]

    for x in range(0,Brick.X_AMOUNT):
        for y in range(0,Brick.Y_AMOUNT):
            new = Brick(x,y)
            bricks.add(new)
    return bricks
