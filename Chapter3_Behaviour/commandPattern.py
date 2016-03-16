# -*- coding:utf-8 -*-


def prRed(prt): print("\033[91m {}\033[00m" .format(prt)),


def prGreen(prt): print("\033[92m {}\033[00m" .format(prt)),


def prYellow(prt): print("\033[93m {}\033[00m" .format(prt)),


def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt)),


def prPurple(prt): print("\033[95m {}\033[00m" .format(prt)),


def prCyan(prt): print("\033[96m {}\033[00m" .format(prt)),


def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt)),


def prBlack(prt): print("\033[98m {}\033[00m" .format(prt)),


class Colors(object):
    RED = "red"
    GREEN = "green"
    PURPLE = "purple"
    YELLOW = "yellow"
    BLACK = "black"

color_print_map = {
    Colors.RED: prRed,
    Colors.GREEN: prGreen,
    Colors.PURPLE: prPurple,
    Colors.YELLOW: prYellow,
    Colors.BLACK: prBlack,
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
            self.__cells[y][x] = color


def callable(function):
    import collections
    # to judge whether a callable instance
    return isinstance(function, collections.Callable)


class Command(object):
    """docstring for Command"""

    def __init__(self, do, undo, description=""):
        assert callable(do) and callable(undo)
        super(Command, self).__init__()
        self.do = do
        self.undo = undo

    def __call__(self):
        self.do()


class Macro(object):
    """docstring for Macro"""

    def __init__(self, description=""):
        super(Macro, self).__init__()
        self.description = description
        self.__commands = []

    def add(self, command):
        if not isinstance(command, Command):
            raise TypeError("Expected object of type Command, got {}".format(
                type(command).__name__))
        self.__commands.append(command)

    def __call__(self):
        for command in self.__commands:
            command()

    do = __call__

    def undo(self):
        for command in reversed(self.__commands):
            command.undo()


class UndoableGrid(Grid):

    def __init__(self, width, height):
        super(UndoableGrid, self).__init__(width, height)

    def create_cell_command(self, x, y, color):
        def undo():
            if undo.__dict__.get('color'):
                self.cell(x, y, undo.color)
            else:
                print "Nothing to undo for the current command"

        def do():
            undo.color = self.cell(x, y)
            self.cell(x, y, color)
        return Command(do, undo, "Cell")

    def create_rectangel_macro(self, x0, y0, x1, y1, color):
        macro = Macro("Rectangle")
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                macro.add(self.create_cell_command(x, y, color))
        return macro


def print_grid(grid):
    if isinstance(grid, Grid):
        for y in range(grid.height):
            for x in range(grid.width):
                color_print_map[grid.cell(x, y)]("█")
            print
    print

if __name__ == "__main__":
    grid = UndoableGrid(4, 4)

    # commands
    command_1 = grid.create_rectangel_macro(0, 0, 3, 3, Colors.RED)
    command_2 = grid.create_rectangel_macro(1, 1, 3, 3, Colors.GREEN)
    command_3 = grid.create_rectangel_macro(2, 2, 3, 3, Colors.PURPLE)

    print_grid(grid)

    print "do command_1"
    command_1()
    print_grid(grid)

    print "do command_2"
    command_2()
    print_grid(grid)

    print "do command_3"
    command_3()
    print_grid(grid)

    print "start to undo"
    print
    print "undo command_3"
    command_3.undo()
    print_grid(grid)

    print "undo command_2"
    command_2.undo()
    print_grid(grid)

    print "undo command_1"
    command_1.undo()
    print_grid(grid)

    # to check the result,
    # check the png file named: fill_color_in_grid_undoable_command.py
