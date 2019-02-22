import pygame
from Snake import Snake
from Apple import Apple
from pygame.locals import *

pygame.init()

SCREEN_SIZE = (500, 400)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
BG = pygame.Surface(SCREEN_SIZE)
BG.fill((0, 0, 0))
SCREEN.blit(BG, (0, 0))

def isSquareHit(p1, p2, buffer):
    ''' (int, int), (int, int), int --> Boolean
    p1 and p2 are tuples each representing an x, y coordinate location of the top left of a square.
    buffer is the size of the square's sides.
    isSquareHit returns True if one square is inside the other. Otherwise False.
    '''
    return p1[0] == p2[0] and p1[1] == p2[1]

class SnakeGame():

    def __init__(self):
        self.running = True
        self.score = 0
        self.snake = Snake(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
        self.apple = Apple()
        self.apple.setPos(SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.scorePosX = SCREEN_SIZE[0] // 2 - 10

    
    def isSnakeCollision(self):
        body = self.snake.getBody()
        head = body[0]
        # check left and righside screen
        if ((head[0] < 0 or head[0] > (SCREEN_SIZE[0] - self.snake.getSize()))):
            #print("Left or Right")
            return True
        # check top and bottom of screen
        if ((head[1] < 0 or head[1] > (SCREEN_SIZE[1] - self.snake.getSize()))):
            #print("Top or Bottom")
            return True
        # check if snake hit self
        if (len(body) > 3):
            for i in range(3, len(body)):
                if isSquareHit(head, body[i], self.snake.getSize()):
                    #print("Body hit " + str(i))
                    #print("Body coord: " + str(body[i][0]) + " " + str(body[i][1]))
                    #print("Head coord: " + str(body[0][0]) + " " + str(body[0][1]))
                    return True
        return False

    def isAppleCollision(self):
        head = self.snake.getBody()[0]
        return isSquareHit((self.apple.getX(), self.apple.getY()), head, self.snake.getSize())

    def drawScore(self, surface):
        scoreFont = pygame.font.Font(None, 40)
        scoreSurface = scoreFont.render(str(self.score), True, (255, 255, 255))
        surface.blit(scoreSurface, (self.scorePosX, 0))


    def play(self):
        pygame.display.flip()

        while self.running:
            SCREEN.blit(BG, (0, 0)) # Makes clean background
            self.apple.drawApple(SCREEN, self.snake.getSize())
            self.snake.drawSnake(SCREEN)
            self.drawScore(SCREEN)
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
            #self.snake.printSnake()
            if self.isSnakeCollision():
                # print("Crashed") # For Testing a bug
                self.snake.drawSnake(SCREEN)
                self.running = False
            if self.isAppleCollision():
                self.apple.setPos(SCREEN_SIZE[0], SCREEN_SIZE[1])
                self.snake.addSegment()
                self.score +=1

            # Game Speed
            pygame.time.delay(80)

def main():
    game = SnakeGame()
    game.play()

if __name__ == '__main__':
    main()