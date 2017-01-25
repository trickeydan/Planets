# Paddle.py
# Trickeydan/PythonScience/BrickBreaker
# D.Trickey 2017
#
# Class file for Paddle

import pygame
from random import randint
from Brick import Brick

class Paddle(pygame.sprite.Sprite):

    WIDTH = 80
    HEIGHT = 20

    SCREEN_WIDTH = Brick.BLOCK_WIDTH * (Brick.X_AMOUNT + 4) + HEIGHT
    SCREEN_HEIGHT = Brick.BLOCK_HEIGHT * (Brick.Y_AMOUNT + 10)

    X = (SCREEN_WIDTH - WIDTH) / 2

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([Paddle.WIDTH,Paddle.HEIGHT])

        self.image.fill((255,51,51))

        self.rect = self.image.get_rect()

        self.rect.x = Paddle.X
        self.rect.y = Paddle.SCREEN_HEIGHT - Paddle.HEIGHT

    def update(self):
        mouse = pygame.mouse.get_pos()
        Paddle.X = mouse[0]
        self.rect.x = Paddle.X - (Paddle.WIDTH / 2)
