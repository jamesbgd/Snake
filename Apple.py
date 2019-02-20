import pygame
import random

class Apple():

    def __init__(self):
        random.seed()
        self.x = None
        self.y = None
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setPos(self, xMax, yMax):
        self.x = (random.randint(0, xMax) // 10) * 10
        self.y = (random.randint(0, yMax) // 10) * 10

    def drawApple(self, surface, size):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, size, size))