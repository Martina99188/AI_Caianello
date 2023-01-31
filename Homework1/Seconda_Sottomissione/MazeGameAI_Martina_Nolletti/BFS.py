# import turtle library
import turtle
import time
import sys
from collections import deque

# define the turtle screen
wn = turtle.Screen()
# set the background colour
wn.bgcolor("black")
wn.title("A BFS Maze Solving Program")
# set up the dimensions of the working window
wn.setup(1300, 700)


# this is the class for the Maze
# define a Maze class
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        # the turtle shape
        self.shape("square")
        # colour of the turtle
        self.color("white")
        # lift the pen so it do not leave a trail
        self.penup()
        self.speed(0)


# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)


class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+           +                 +              s++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]


# define a function called setup_maze
def setup_maze(grid):
    # set up global variables for start and end locations
    global start_x, start_y, end_x, end_y
    # read in the grid line by line
    for y in range(len(grid)):
        # read each cell in the line
        for x in range(len(grid[y])):
            # assign the variable "character" the x and y location od the grid
            character = grid[y][x]
            # move to the x location on the screen staring at -588
            screen_x = -588 + (x * 24)
            # move to the y location of the screen starting at 288
            screen_y = 288 - (y * 24)

            if character == "+":
                # move pen to the x and y location and
                maze.goto(screen_x, screen_y)
                # stamp a copy of the turtle on the screen
                maze.stamp()
                # add coordinate to walls list
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                # add " " and e to path list
                path.append((screen_x, screen_y))

            if character == "e":
                green.color("purple")
                # send green sprite to screen location
                green.goto(screen_x, screen_y)
                # assign end locations variables to end_x and end_y
                end_x, end_y = screen_x, screen_y
                green.stamp()
                green.color("green")

            if character == "s":
                # assign start locations variables to start_x and start_y
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()


def searchBFS(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    # exit while loop when frontier queue equals zero
    while len(frontier) > 0:
        time.sleep(0)
        # pop next entry in the frontier queue an assign to x and y location
        x, y = frontier.popleft()

        # check the cell on the left
        if (x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            # backtracking routine [cell] is the previous cell. x, y is the current cell
            solution[cell] = x, y
            # add cell to frontier list
            frontier.append(cell)
            # add cell to visited list
            visited.add((x - 24, y))

        # check the cell down
        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 24))

        # check the cell on the  right
        if (x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x + 24, y))

        # check the cell up
        if (x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()


def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    # stop loop when current cells == start cell
    while (x, y) != (start_x, start_y):
        # move the yellow sprite to the key value of solution ()
        yellow.goto(solution[x, y])
        yellow.stamp()
        # "key value" now becomes the new key
        x, y = solution[x, y]


# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
# solution dictionary
solution = {}

# declare system variables
start_x = 0
start_y = 0
end_x = 0
end_y = 0

if __name__ == '__main__':
    # main program starts here ####
    setup_maze(grid)
    searchBFS(start_x, start_y)
    backRoute(end_x, end_y)
    wn.exitonclick()
