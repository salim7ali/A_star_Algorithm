from spot import make_grid, show_grid

BLACK = (0, 0, 0)        # background   0
WHITE = (255, 255, 255)  # normal tile  1
BROWN = (210,105,30)     # wall         2
ORANGE = (255,165,0)     # path         3
GREEN = (0, 255, 0)      # end node     4
RED = (255, 0, 0)        # start node   5

class AStar:
    # F(n) = g(n) + h(n)
    def __init__(self):
        self.grid = make_grid()
        # self.grid[0][0].set_as_start_node()
        # self.grid[3][2].set_as_end_node()

    # def check_adjacent_nodes(self):
    #     if

if __name__ == "__main__":
    # grid = [[5, 1, 1, 1],
    #         [1, 1, 1, 1],
    #         [1, 1, 1, 1],
    #         [1, 1, 4, 1]]

    # show_grid(grid)

    algo_obj = AStar()

