# -*- coding:utf-8 -*-

def prRed(prt): print("\033[91m {}\033[00m" .format(prt)),
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt)),
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt)),
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt)),
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt)),
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt)),
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt)),
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt)),

color_print_map = {
    "red": prRed,
    "green": prGreen,
    "purple": prPurple,
    "yellow": prYellow,
    "black": prBlack,
}

class Grid(object):
    """docstring for Grid"""
    def __init__(self, width, height, random_flag=False):
        from random import choice
        super(Grid, self).__init__()
        self.width = width 
        self.height = height
        if not random_flag:
            self.__cells = [["black" for _ in range(width)]
                            for _ in range(height)]
        else:
            self.__cells = [[choice(color_print_map.keys()) for _ in range(width)]
                            for _ in range(height)]

    def cell(self, x, y, color=None):
        if color is None:
            return self.__cells[y][x]
        else:
            self.__cells[y][x]=color

def color_print(grid):
    if isinstance(grid, Grid):
        for y in range(grid.height):
            for x in range(grid.width):
                color_print_map[grid.cell(x,y)]("█")
            print 

if __name__ == "__main__":
    grid = Grid(15, 15, True)
    color_print(grid)


