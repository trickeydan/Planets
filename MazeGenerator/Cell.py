# Cell.py
# Trickeydan/PythonScience/MazeGenerator
# D.Trickey 2017
#
# This class represents a cell on the grid.
# This file also contains get_cell_num

import pygame, random

def get_cell_num(x,y):
    if x < 0 or y < 0 or x > Cell.GRID_NUM - 1 or y > Cell.GRID_NUM - 1:
        return 0
    return Cell.GRID_NUM * y + x

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,51,51)

class Cell():

    CELL_SIZE = 60 # The width of a cell in pixels.
    GRID_NUM = 10  # The number of cells to have as the width and height.

    def __init__(self,grid_x,grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.pixel_x = grid_x * Cell.CELL_SIZE
        self.pixel_y = grid_y * Cell.CELL_SIZE
        self.walls = [True,True] # Has walls - [Top,Left]
        self.visited = False # Not visited initially.

    def draw(self,screen):
        if self.visited:
            #If this cell has been visited, colour it red.
            pygame.draw.rect(screen,RED,[self.pixel_x,self.pixel_y,Cell.CELL_SIZE,Cell.CELL_SIZE])

        if self.walls[0]:
            pygame.draw.line(screen,BLACK,[self.pixel_x,self.pixel_y],[self.pixel_x+Cell.CELL_SIZE,self.pixel_y],2) # Draw the top line of a cell
        if self.walls[1]:
            pygame.draw.line(screen,BLACK,[self.pixel_x,self.pixel_y],[self.pixel_x,self.pixel_y+Cell.CELL_SIZE],2) # Draw the left line of a cell

    def getNext(self,grid):
        # So, this instance is the current cell.
        # Get the cells around me.
        neighbours = []
        neighbours.append(grid[get_cell_num(self.grid_x,self.grid_y - 1)]) # Top
        neighbours.append(grid[get_cell_num(self.grid_x + 1,self.grid_y)]) # Right
        neighbours.append(grid[get_cell_num(self.grid_x,self.grid_y + 1)]) # Bottom
        neighbours.append(grid[get_cell_num(self.grid_x - 1,self.grid_y)]) # Left

        # Look in the cells around me to see if any haven't been visited.

        unvisited = []

        for cell in neighbours:
            if not cell.visited:
                unvisited.append(cell)
        if len(unvisited) <= 0:
            return None
        return random.choice(unvisited)

    def removeWall(self,adjacentCell):
        # Remove the wall if on this cell that corresponds to the adjacentCell
        if adjacentCell.grid_x == self.grid_x and adjacentCell.grid_y == self.grid_y -1:
            self.walls[0] = False #Remove the top wall
        elif adjacentCell.grid_x == self.grid_x - 1 and adjacentCell.grid_y == self.grid_y:
            self.walls[1] = False #Remove the left wall
