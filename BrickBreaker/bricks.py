# bricks.py
# Trickeydan/PythonScience/BrickBreaker
# D.Trickey 2017
#
# A brick breaker style arcade game.

import pygame
from Brick import *
from Paddle import Paddle
from Text import Text
from Ball import Ball

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,51,51)

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = Brick.BLOCK_WIDTH * (Brick.X_AMOUNT + 4) + Paddle.HEIGHT
screen_height = Brick.BLOCK_HEIGHT * (Brick.Y_AMOUNT + 10)
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Brick Breaker")

text = []

title = Text([1,1],BLACK)
title.text = "Brick Breaker"

levelText = Text([1,1 + title.height()],BLACK)
scoreText = Text([1,1 + title.height() * 2],BLACK)

all_sprites = pygame.sprite.Group()

bricks = generateBricks()
paddle = Paddle()
ball = Ball()

all_sprites.add(paddle)
all_sprites.add(ball)

clock = pygame.time.Clock()
playing = False #Is the ball moving?
done = False
score = 0
level = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not playing:
            playing = True
            ball.attached = False

    all_sprites.update()

    if ball.belowPaddle():
        playing = False
        ball.attached = True
        ball.reset()
        print("Death")

    bricks_hit = pygame.sprite.spritecollide(ball,bricks, True) # Check collisions and remove any hit from all groups
    score += len(bricks_hit)
    if len(bricks_hit) > 0:
        # Choose which direction(s) to reverse
        gamma = bricks_hit[0]
        # Y direction
        if ball.rect.y + Ball.DIAMETER >= gamma.rect.y or ball.rect.y <= gamma.rect.y + Brick.BLOCK_HEIGHT :
            ball.yVel *= -1

    if len(bricks) <= 0:
        # Level Up!
        level += 1
        bricks = generateBricks()
        ball.vMag *= level
        playing = False
        ball.attached = True
        ball.reset()

    bricks.update()

    scoreText.text = "Score: " + str(score)
    levelText.text = "Level " + str(level)

    screen.fill(WHITE)
    bricks.draw(screen)
    all_sprites.draw(screen)

    title.render(screen)
    levelText.render(screen)
    scoreText.render(screen)

    clock.tick(60) # 60FPS
    pygame.display.flip()

pygame.quit()
