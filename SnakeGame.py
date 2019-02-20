import pygame
from Snake import Snake
from Apple import Apple
from pygame.locals import *

pygame.init()

SCREEN_SIZE = (500, 300)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
BG = pygame.Surface(SCREEN_SIZE)
BG.fill((0, 0, 0))
SCREEN.blit(BG, (0, 0))

def isSquareHit(p1, p2, buffer):
    ''' (int, int), (int, int), int --> Boolean
    p1 and p2 are tuples each representing an x, y coordinate location of the top left of a square.
    buffer is the size of the square's sides.
    rectHit returns True if one square is inside the other. Otherwise False.
    '''
    if ((p1[0] >= p2[0]) and (p1[0] <= p2[0] + buffer)):
        if ((p1[1] >= p2[1]) and (p1[1] <= p2[1] + buffer)):
            return True
    return False

class SnakeGame():

    def __init__(self):
        self.running = True
        self.score = 0
        self.snake = Snake(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
        self.apple = Apple()
        self.apple.setPos(SCREEN_SIZE[0], SCREEN_SIZE[1])

    
    def snakeCollision(self):
        body = self.snake.getBody()
        head = body[0]
        # check left and righside screen
        if ((head[0] < 0 or head[0] > (SCREEN_SIZE[0] - self.snake.getSize()))):
            return True
        # check top and bottom of screen
        if ((head[1] < 0 or head[1] > (SCREEN_SIZE[1] - self.snake.getSize()))):
            return True
        # check if snake hit self
        if (len(body) > 3):
            for i in range(3, len(body) - 1):
                if isSquareHit(head, body[i], self.snake.getSize()):
                    return True
        return False

    def appleCollision(self):
        head = self.snake.getBody()[0]
        return isSquareHit((self.apple.getX(), self.apple.getY()), head, self.snake.getSize())

    def play(self):
        pygame.display.flip()

        while self.running:
            SCREEN.blit(BG, (0, 0)) # Makes clean background
            self.apple.drawApple(SCREEN, self.snake.getSize())
            self.snake.drawSnake(SCREEN)
            pygame.display.flip()

            # Move the snake
            self.snake.moveSnake()

            # Handle Key events
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                elif event.type == QUIT:
                    self.running = False
                    pygame.quit()
            pressedKeys = pygame.key.get_pressed()
            self.snake.changeDir(pressedKeys)
            
            # Handle Collisions
            if self.snakeCollision():
                self.running = False
            if self.appleCollision():
                self.apple.setPos(SCREEN_SIZE[0], SCREEN_SIZE[1])
                self.snake.addSegment()
                self.score +=1

            # Game Speed
            pygame.time.delay(20)

def main():
    game = SnakeGame()
    game.play()

if __name__ == '__main__':
    main()