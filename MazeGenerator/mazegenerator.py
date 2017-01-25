# mazegenerator.py
# Trickeydan/PythonScience/MazeGenerator
# D.Trickey 2017
#
# Generates a random maze with only one valid path using the depth-first algorithm.

import pygame
from Cell import *

showSol = True
graphics = True

screen_width = Cell.CELL_SIZE * (Cell.GRID_NUM + 2)
screen_height = screen_width

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Maze Generator")

clock = pygame.time.Clock()
done = False # If true, then end the program.
complete = False # If true, then the maze has been drawn.

grid = []

# Put cells in grid
for y in range(0,Cell.GRID_NUM):
    for x in range(0,Cell.GRID_NUM):
        #print(get_cell_num(grid_width,x,y))
        grid.append(Cell(x,y)) #Add a new cell to the grid array.

grid[len(grid) -2].visited = True # Prevents it continuing at the end.
grid[len(grid) -2].walls = [False,True]

stack = []

current = grid[0] # Set the current cell to the far top left cell.
sofar = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    if not complete:
        current.visited = True
        sofar += 1
        if current == grid[len(grid) -1] and showSol:
            #STOP! Time to make the solution
            for sol in stack:
                grid[sol.num].solution = True


        nextCell = current.getNext(grid)
        if type(nextCell) != type(None):
            stack.append(current)
            current.removeWall(nextCell)
            nextCell.removeWall(current)
            current = nextCell
        else:
            if len(stack) == 0:
                complete = True
            else:
                current = stack.pop()

        if graphics:
            screen.fill(WHITE)
            for cell in grid:
                if cell == current:
                    cell.draw(screen,GREEN) # Draw every cell.
                else:
                    cell.draw(screen,RED) # Draw every cell.
            pygame.draw.rect(screen,BLACK,[Cell.CELL_SIZE,Cell.CELL_SIZE,Cell.CELL_SIZE * Cell.GRID_NUM,Cell.CELL_SIZE * Cell.GRID_NUM],2)
            clock.tick(120)
            pygame.display.flip()
        else:
            print("{0:.2f}".format(sofar * 50 / (Cell.GRID_NUM ** 2)) + "%")
    else:
        screen.fill(WHITE)
        for cell in grid:
            cell.draw(screen,WHITE) # Draw every cell.
        pygame.draw.rect(screen,BLACK,[Cell.CELL_SIZE,Cell.CELL_SIZE,Cell.CELL_SIZE * Cell.GRID_NUM,Cell.CELL_SIZE * Cell.GRID_NUM],2)

        clock.tick(120)
        pygame.display.flip()

pygame.quit()
