import pygame
import random
from spot import make_grid, show_grid, displacement_bw_nodes
import heapq as hq
# from algorithm import AStar

class InterfaceGrid:
    BLACK = (0, 0, 0)        # background   0
    WHITE = (255, 255, 255)  # normal tile  1
    BROWN = (210,105,30)     # wall         2
    ORANGE = (255,165,0)     # path         3
    GREEN = (0, 255, 0)      # end node     4
    RED = (255, 0, 0)        # start node   5

    NO_OF_WALLS = 20

    WIDTH = 20
    HEIGHT = 20
    MARGIN = 5
    start_node_set = False
    end_node_set = False

    wall_count = 0

    start_node = ()
    end_node = ()

    f_prior_q = dict()
    f_dict = dict()
    
    def __init__(self, WINDOW_SIZE):
        self.setup_pygame(WINDOW_SIZE)
        self.grid = make_grid()
        # print(self.grid)

    def setup_pygame(self, WINDOW_SIZE):
        self.WINDOW_SIZE = WINDOW_SIZE
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("A* algorithm Implementation Grid")
        self.clock = pygame.time.Clock()
        
    def get_user_input(self):
        global grid_filled
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                global close_window
                close_window = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN and self.wall_count<self.NO_OF_WALLS:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (self.WIDTH + self.MARGIN)
                row = pos[1] // (self.HEIGHT + self.MARGIN)
                # Set that location to one
                if not self.start_node_set:
                    self.grid[row][column].set_as_start_node()
                    self.start_node_set = True
                    self.add_to_heap(0, row, column)
                    self.start_node = (row, column)
                elif not self.end_node_set:
                    self.grid[row][column].set_as_end_node()
                    self.end_node_set = True
                    self.end_node = (row, column)
                elif not((row == self.start_node[0] and column == self.start_node[1]) or \
                    (row == self.end_node[0] and column == self.end_node[1])): # wall
                    # import pdb;pdb.set_trace()
                    self.grid[row][column].set_as_wall()
                    self.wall_count += 1
            elif self.wall_count >=self.NO_OF_WALLS and grid_filled==False:
                for row in range(10):
                    for column in range(10):   
                        self.grid[row][column].set_neighbours(row, column, self.grid)
                grid_filled = True
                # print("Click ", pos, "Grid coordinates: ", row, column)
    
    def show_result_path(self):
        row = self.end_node[0]
        column = self.end_node[1]
        # while (row, column) != self.start_node:
        while True:
            print(f"({row}, {column}) -> ", end=' ')
            try:
                (row, column) = self.grid[row][column].prev_node
                if (row, column) != self.start_node:
                    self.grid[row][column].node_type = 'P'
            except ValueError:
                break
            

            

    def add_to_heap(self, f, row, column):
        self.f_dict[f] = (row, column)
        self.f_prior_q = list(self.f_dict.items())
        hq.heapify(self.f_prior_q)
        self.f_prior_q = dict(self.f_prior_q)
        print("(2)",self.f_prior_q)

    def extract_min_from_heap(self ):
        f = list(self.f_prior_q.keys())[0]
        coordinates = self.f_prior_q[f]

        self.f_dict.pop(f)
        self.f_prior_q.pop(f)
        print("(3)",self.f_prior_q)

        return f, coordinates[0], coordinates[1]

    def delete_from_heap(self, f):
        # import pdb;pdb.set_trace()
        self.f_dict.pop(f, None)
        self.f_prior_q.pop(f, None)


        
    def draw_grid(self):
        self.screen.fill(self.BLACK)

        for row in range(10):
            for column in range(10):
                color = self.WHITE
                if self.grid[row][column].node_type == 'N':
                    color = self.WHITE
                elif self.grid[row][column].node_type == 'W':
                    color = self.BROWN
                elif self.grid[row][column].node_type == 'P':
                    color = self.ORANGE
                elif self.grid[row][column].node_type == 'E':
                    color = self.GREEN
                elif self.grid[row][column].node_type == 'S':
                    color = self.RED
                
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.MARGIN+self.WIDTH)*column + self.MARGIN,
                                 (self.MARGIN+self.HEIGHT)*row + self.MARGIN,
                                 self.WIDTH, 
                                 self.HEIGHT] )
                     


import pdb
if __name__ == '__main__':
    gridObj = InterfaceGrid([255, 255])
    grid_filled = False

    close_window = False
    while not close_window:
        gridObj.get_user_input()
        gridObj.draw_grid()
        gridObj.clock.tick(60)
        pygame.display.flip()

        # try:
        while len(gridObj.f_prior_q) and grid_filled:
            # pdb.set_trace()
            f, row, column = gridObj.extract_min_from_heap()
            # pdb.set_trace()
            for neigh_row, neigh_col in gridObj.grid[row][column].neighbours:
                if (gridObj.grid[neigh_row][neigh_col].fixed == False) and \
                    (gridObj.grid[neigh_row][neigh_col].g > gridObj.grid[row][column].g+1):
                    print("(1)")
                    gridObj.delete_from_heap(gridObj.grid[neigh_row][neigh_col].f)
                    gridObj.grid[neigh_row][neigh_col].g = gridObj.grid[row][column].g+1
                    gridObj.grid[neigh_row][neigh_col].h = displacement_bw_nodes((neigh_row, neigh_col), gridObj.end_node)
                    gridObj.grid[neigh_row][neigh_col].update_f()
                    gridObj.grid[neigh_row][neigh_col].prev_node = (row, column)
                    gridObj.add_to_heap(gridObj.grid[neigh_row][neigh_col].f, neigh_row, neigh_col)
            show_grid(gridObj.grid)
            gridObj.show_result_path()
        # except:
        #     pdb.set_trace()

    pygame.quit()