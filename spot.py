from math import sqrt, ceil
MAX_ROW = 10
MAX_COLUMN = 10
# MAX_SIZE = 10
class GraphNode:
    MAX_DIST = 9999999

    def __init__(self, row, column, node_type='N'):
        self.node_type = node_type
        self.prev_node = ()
        self.fixed = False

        self.g = self.MAX_DIST
        self.h = self.MAX_DIST
        self.f = self.MAX_DIST
        self.neighbours = []

    def set_neighbours(self, i, j, grid):
        if j+1<MAX_COLUMN and grid[i][j].node_type != 'W' :
            # RIGHT
            self.neighbours.append((i, j+1))
        if i+1<MAX_ROW and grid[i][j].node_type != 'W':
            # BOTTOM
            self.neighbours.append((i+1, j))
        if j-1>=0 and grid[i][j].node_type != 'W':
            # LEFT
            self.neighbours.append((i, j-1))
        if i-1>=0 and grid[i][j].node_type != 'W':
            # TOP
            self.neighbours.append((i-1, j))

    
    # def get_node_type(self):
    #     return self.node_type

    def update_f(self):
        self.f = self.g+self.h

    def set_as_start_node(self):
        self.node_type = 'S'
        self.g = 0
        # self.h = 0
        # self.f = 0

    def set_as_end_node(self):
        self.node_type = 'E'
        # self.g = displacement_bw_nodes()
        self.h = 0
        self.f = 0

    def set_as_wall(self):
        self.node_type = 'W'
        # self.g = displacement_bw_nodes()
        self.h = 0
        # self.f = 0

def displacement_bw_nodes(node_a, node_b):
    b_col_minus_a_col_squared = (node_b[1] - node_a[1])**2
    b_row_minus_a_row_squared = (node_b[0] - node_a[0])**2
    displacement = sqrt(b_col_minus_a_col_squared + b_row_minus_a_row_squared)
    return displacement

# class Graph:
def make_grid():
    grid = []
    temp = []
    for row in range(10):
        for column in range(10):   
            temp.append(GraphNode(row, column))
        grid.append(temp)
        temp = []
    return grid

def show_grid(grid):
    for row in range(10):
        for column in range(10):   
            print(grid[row][column].node_type, end=' ')
        print()
