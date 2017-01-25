# Ball.py
# Trickeydan/PythonScience/BrickBreaker
# D.Trickey 2017
#
# Class file for Ball

import pygame
from random import randint, choice
from Brick import Brick
from Paddle import Paddle

class Ball(pygame.sprite.Sprite):

    DIAMETER = 16

    def __init__(self):
        super().__init__()

        self.radius = int(Ball.DIAMETER // 2)

        self.image = pygame.Surface([Ball.DIAMETER,Ball.DIAMETER])
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image,(51,255,51),[self.radius,self.radius],self.radius)

        self.rect = self.image.get_rect()

        self.attached = True
        self.vMag = 3 # Magnitude of the ball's velocity.
        self.reset()

    def reset(self):
        self.xVel = choice([-1,1])# These variables specify the direction of the ball. X-dir is random
        self.yVel = -1



    def update(self):
        if self.attached:
            mouse = pygame.mouse.get_pos()
            self.rect.x = mouse[0] - self.radius
            self.rect.y = Brick.BLOCK_HEIGHT * (Brick.Y_AMOUNT + 10) - Paddle.HEIGHT - Ball.DIAMETER
        else:
            # Update position
            self.rect.x += self.xVel * self.vMag
            self.rect.y += self.yVel * self.vMag

            # Check if edges hit and bounce
            if self.rect.x < 0 or self.rect.x > Paddle.SCREEN_WIDTH - Ball.DIAMETER:
                self.xVel *= -1
            if self.rect.y < 0:
                self.yVel *= -1

            if self.rect.y + Ball.DIAMETER >= Paddle.SCREEN_HEIGHT - Paddle.HEIGHT and self.rect.x + Ball.DIAMETER > Paddle.X \
            and self.rect.x < Paddle.X + Paddle.WIDTH:
                self.rect.y = Brick.BLOCK_HEIGHT * (Brick.Y_AMOUNT + 10) - Paddle.HEIGHT - Ball.DIAMETER - 1
                self.yVel *= -1

    def belowPaddle(self):
        return self.rect.y > Paddle.SCREEN_HEIGHT
