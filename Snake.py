import pygame
from pygame.locals import *

pygame.init()
MAX_VEL = 10
TEST = 400

class Snake():

    def __init__(self, startX, startY):
        self.xVel = 0
        self.yVel = -MAX_VEL
        self.snakeSize = 10 # length and width of each segment (square)
        self.lastPos = None

        self.surf = pygame.Surface((self.snakeSize, self.snakeSize))
        self.surf.fill((255,255,255))

        self.body = ([(startX - self.snakeSize, startY - self.snakeSize),
                     (startX - self.snakeSize, startY)])
    
    def getSize(self):
        return self.snakeSize

    def changeDir(self, keyEvent):
        """ keEvent --> Bool
        changeDir takes a pygame KEYDOWN event and changes the direction of
        the Snake if the event was an arrow key.
        The boolean return tells whether the direction was changed or not.
        """
        didChangeDir = False
        if keyEvent.key == K_UP and self.yVel != MAX_VEL:
            self.xVel = 0
            self.yVel = -MAX_VEL
            didChangeDir = True
        elif keyEvent.key == K_DOWN and self.yVel != -MAX_VEL:
            self.xVel = 0
            self.yVel = MAX_VEL
            didChangeDir = True
        elif keyEvent.key == K_LEFT and self.xVel != MAX_VEL:
            self.xVel = -MAX_VEL
            self.yVel = 0
            didChangeDir = True
        elif keyEvent.key == K_RIGHT and self.xVel != -MAX_VEL:
            self.xVel = MAX_VEL
            self.yVel = 0
            didChangeDir = True
        return didChangeDir

    def moveSnake(self):
        self.lastPos =  self.body[-1]
        oldHead = self.body[0]
        newHead = (oldHead[0] + self.xVel, oldHead[1] + self.yVel)
        self.body = [newHead] + self.body[: len(self.body) - 1]
    
    def addSegment(self):
        self.body += [self.lastPos]

    def drawSnake(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (255, 255, 255), (segment[0], segment[1], self.snakeSize, self.snakeSize))

    def printSnake(self):
        for i in range(0, len(self.body)):
            print("Segment " + str(i) + " coordinate: " + str(self.body[i]))

    def getBody(self):
        return self.body