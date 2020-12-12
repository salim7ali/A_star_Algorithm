import pygame
import random

class Grid:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    WIDTH = 20
    HEIGHT = 20

    MARGIN = 5
    
    def __init__(self, WINDOW_SIZE):
        self.setup_pygame(WINDOW_SIZE)
        self.grid = [[random.randint(1,2) for y in range(10)] for x in range(10)]
        self.grid[5][1] = 2
        print(self.grid)

    def setup_pygame(self, WINDOW_SIZE):
        self.WINDOW_SIZE = WINDOW_SIZE
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("A* algorithm Implementation Grid")
        self.clock = pygame.time.Clock()
        
    def get_user_input(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                global done
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (self.WIDTH + self.MARGIN)
                row = pos[1] // (self.HEIGHT + self.MARGIN)
                # Set that location to one
                self.grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
        
    def draw_grid(self):
        self.screen.fill(self.BLACK)

        for row in range(10):
            for column in range(10):
                color = self.WHITE
                if self.grid[row][column] == 1:
                    color = self.GREEN
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.MARGIN+self.WIDTH)*column + self.MARGIN,
                                 (self.MARGIN+self.HEIGHT)*row + self.MARGIN,
                                 self.WIDTH, 
                                 self.HEIGHT] )
                     



if __name__ == '__main__':
    gridObj = Grid([255, 255])

    done = False
    while not done:
        gridObj.get_user_input()
        gridObj.draw_grid()
        gridObj.clock.tick(60)
        pygame.display.flip()

    
    pygame.quit()