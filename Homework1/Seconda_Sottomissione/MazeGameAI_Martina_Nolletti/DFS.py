import turtle
import time

# define the turtle screen
display = turtle.Screen()
# set the background colour
display.bgcolor("black")
display.title("A DFS Maze Solving Program")
# set up the dimensions of the working window
display.setup(1300, 700)

# declare system variables
start_x = 0
start_y = 0
end_x = 0
end_y = 0


# the five classes below are drawing turtle images to construct the maze.
# use white turtle to stamp out the maze
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
        # define the animation speed
        self.speed(0)


# use green turtles to show the visited cells
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


# use blue turtle to show the frontier cells
class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# use the red turtle to represent the start position
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        # point turtle to point down
        self.setheading(270)
        self.penup()
        self.speed(0)


# use the yellow turtle to represent the end position and the solution path
class Yellow(turtle.Turtle):  # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


grid = [
    "++++++++++++++++++++++++++++++++++++++++++++++",
    "+ s             +                            +",
    "+ +++++++++++ +++++++++++++++ ++++++++ +++++ +",
    "+           +                 +        +     +",
    "++ +++++++ ++++++++++++++ ++++++++++++++++++++",
    "++ ++    + ++           + ++                 +",
    "++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
    "++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
    "++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
    "++ ++   ++ ++             ++          +++ ++e+",
    "++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
    "++    + ++                   ++              +",
    "+++++ + +++++++++++++++++++++++ ++++++++++++ +",
    "++ ++ +                   ++          +++ ++ +",
    "++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
    "++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
    "++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
    "++                     ++ ++ ++              +",
    "+++++ ++ + +++++++++++ ++ ++ ++ ++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++",
]


# this function constructs the maze based on the grid type above
def setup_maze(grid):
    # set up global variables for start and end locations
    global start_x, start_y, end_x, end_y
    # iterate through each line in the grid
    for y in range(len(grid)):
        # iterate through each character in the line
        for x in range(len(grid[y])):
            # assign the variable character to the y and x positions of the grid
            character = grid[y][x]
            # move to the x location on the screen staring at -288
            screen_x = -588 + (x * 24)
            # move to the y location of the screen starting at 288
            screen_y = 288 - (y * 24)

            # if character contains a '+'
            if character == "+":
                # move pen to the x and y location and
                maze.goto(screen_x, screen_y)
                # stamp a copy of the white turtle on the screen
                maze.stamp()
                # add cell to the walls list
                walls.append((screen_x, screen_y))

            # if no character found
            if character == " ":
                # add to path list
                path.append((screen_x, screen_y))

            # if cell contains an 'e'
            if character == "e":
                # move pen to the x and y location and
                yellow.goto(screen_x, screen_y)
                # stamp a copy of the yellow turtle on the screen
                yellow.stamp()
                # assign end locations variables to end_x and end_y
                end_x, end_y = screen_x, screen_y
                # add cell to the path list
                path.append((screen_x, screen_y))

            # if cell contains a "s"
            if character == "s":
                # assign start locations variables to start_x and start_y
                start_x, start_y = screen_x, screen_y
                # send red turtle to start position
                red.goto(screen_x, screen_y)


def searchDFS(x, y):
    # add the x and y position to the frontier list
    frontier.append((x, y))
    # add x and y to the solution dictionary
    solution[x, y] = x, y
    # loop until the frontier list is empty
    while len(frontier) > 0:
        # change this value to make the animation go slower
        time.sleep(0)
        # current cell equals x and  y positions
        current = (x, y)

        # check left
        if (x - 24, y) in path and (x - 24, y) not in visited:
            cell_left = (x - 24, y)
            # backtracking routine [cell] is the previous cell. x, y is the current cell
            solution[cell_left] = x, y
            # blue turtle goto the cell_left position
            blue.goto(cell_left)
            # stamp a blue turtle on the maze
            blue.stamp()
            # add cell_left to the frontier list
            frontier.append(cell_left)

        # check down
        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell_down = (x, y - 24)
            # backtracking routine [cell] is the previous cell. x, y is the current cell
            solution[cell_down] = x, y
            blue.goto(cell_down)
            blue.stamp()
            frontier.append(cell_down)

        # check right
        if (x + 24, y) in path and (x + 24, y) not in visited:
            cell_right = (x + 24, y)
            # backtracking routine [cell] is the previous cell. x, y is the current cell
            solution[cell_right] = x, y
            blue.goto(cell_right)
            blue.stamp()
            frontier.append(cell_right)

        # check up
        if (x, y + 24) in path and (x, y + 24) not in visited:
            cell_up = (x, y + 24)
            # backtracking routine [cell] is the previous cell. x, y is the current cell
            solution[cell_up] = x, y
            blue.goto(cell_up)
            blue.stamp()
            frontier.append(cell_up)

        # remove last entry from the frontier list and assign to x and y
        x, y = frontier.pop()
        # add current cell to visited list
        visited.append(current)
        # green turtle goto x and y position
        green.goto(x, y)
        # stamp a copy of the green turtle on the maze
        green.stamp()
        # makes sure the yellow end turtle is still visible after being visited
        if (x, y) == (end_x, end_y):
            # stamp the yellow turtle at the end position
            yellow.stamp()
        # makes sure the red start turtle is still visible after being visited
        if (x, y) == (start_x, start_y):
            # stamp the red turtle at the start position
            red.stamp()


# this is the solution path function
def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    # stop loop when current cells == start cell
    while (x, y) != (start_x, start_y):
        # move the yellow turtle to the key value of solution ()
        yellow.goto(solution[x, y])
        # create solution path
        yellow.stamp()
        # "key value" now becomes the new key
        x, y = solution[x, y]


#  initialise lists
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = []
frontier = []
solution = {}


if __name__ == '__main__':
    # call setup maze function
    setup_maze(grid)
    # call search function
    searchDFS(start_x, start_y)
    # call back route function
    backRoute(end_x, end_y)

# exit out Pygame when x is clicked
display.exitonclick()
