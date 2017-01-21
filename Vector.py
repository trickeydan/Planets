import math, pygame
class Vector():

    def __init__(self,vect):
        self.x = vect[0]
        self.y = vect[1]

    def magnitude(self):
        pythag = (self.x ** 2) + (self.y ** 2)
        return pythag ** 0.5

    def __add__(self,vect):
        return Vector([self.x + vect.x,self.y + vect.y])

    def add(self,vect):
        return self + vect

    def __iadd__(self,vect):
        self.x += vect.x
        self.y += vect.y

    def __sub__(self,vect):
        return Vector([self.x - vect.x,self.y - vect.y])

    def subtract(self,vect):
        return self - vect

    def __mul__(self,scalar):
        return Vector([self.x * scalar,self.y * scalar])

    def mult(self,scalar):
        return self * scalar

    def divide(self,scalar):
        return Vector([self.x / scalar,self.y / scalar])

    def __str__(self):
        return "Vector: x= " + str(self.x) + " y=" + str(self.y)

    def tuple(self):
        return [self.x,self.y]

    def draw(self,surface,pos):
        pygame.draw.line(surface,(255,255,255),self.mult(5).add(pos).tuple(),pos.tuple(),1)
