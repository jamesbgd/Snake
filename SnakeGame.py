import pygame
from Snake import Snake
from Apple import Apple
from pygame.locals import *

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
        self.score = 0
        self.snake = Snake(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
        self.apple = Apple()
        self.apple.placeApple(self.snake.getBody(), SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.scorePosX = SCREEN_SIZE[0] // 2 - 10

    def reset(self):
        self.score = 0
        self.snake = Snake(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
        self.apple.placeApple(self.snake.getBody(), SCREEN_SIZE[0], SCREEN_SIZE[1])

    def isSnakeCollision(self):
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
            for i in range(3, len(body)):
                if isSquareHit(head, body[i], self.snake.getSize()):
                    return True
        return False

    def isAppleCollision(self):
        head = self.snake.getBody()[0]
        return isSquareHit((self.apple.getX(), self.apple.getY()), head, self.snake.getSize())

    def drawScore(self, surface):
        scoreFont = pygame.font.Font(None, 40)
        scoreSurface = scoreFont.render(str(self.score), True, (255, 255, 255))
        surface.blit(scoreSurface, (self.scorePosX, 0))

    def drawSplashScreen(self, surface, text, color):
        ''' Surface, String --> void
        Draws text centered at the center of the given Surface.
        '''
        splashFont = pygame.font.Font(None, 100)
        splashSurface = splashFont.render(text, True, color)
        textXPos = (SCREEN_SIZE[0] // 2) - (splashFont.size(text)[0] // 2)
        textYpos = (SCREEN_SIZE[1] // 2) - (splashFont.size(text)[1] // 2)
        surface.blit(splashSurface, (textXPos, textYpos))

    def handleQuit(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
        elif event.type == QUIT:
            pygame.quit()
            exit()

    def play(self):
        self.drawSplashScreen(SCREEN, "SNAKE", (255, 255, 255))
        pygame.display.flip()
        while True: # starting splashcreen
            event = pygame.event.wait()
            self.handleQuit(event)
            if event.type == KEYDOWN:
                break

        while True:#self.playing: # main loop for running the game
            SCREEN.blit(BG, (0, 0)) # Makes clean background
            self.apple.drawApple(SCREEN, self.snake.getSize())
            self.snake.drawSnake(SCREEN)
            self.drawScore(SCREEN)
            pygame.display.flip()

            # Move the snake
            self.snake.moveSnake()

            # Handle Key events
            for event in pygame.event.get():
                self.handleQuit(event)
            pressedKeys = pygame.key.get_pressed()
            self.snake.changeDir(pressedKeys)
            
            # Handle Collisions
            if self.isSnakeCollision():
                self.snake.drawSnake(SCREEN) # update the snake's position to when it crashed
                self.drawSplashScreen(SCREEN, "GAME OVER", (169, 169, 169))
                pygame.display.flip()
                while True: # game over screen
                    event = pygame.event.wait()
                    self.handleQuit(event)
                    if event.type == KEYDOWN:
                        self.reset()
                        break
            if self.isAppleCollision():
                self.apple.placeApple(self.snake.getBody(), SCREEN_SIZE[0], SCREEN_SIZE[1])
                self.snake.addSegment()
                self.score +=1

            # Game Speed
            pygame.time.delay(80)

def main():
    pygame.init()
    while True:
        game = SnakeGame()
        game.play()

if __name__ == '__main__':
    main()