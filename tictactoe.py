"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import * #Imports all functions from the Turtle module for graphics

from freegames import line #Imports the 'line' function from the Freegames module


def grid():
    """Draw tic-tac-toe grid."""
    #Draw the vertical lines
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    #Draw the horizontal lines
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    ## Draw the two lines of the X
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Draw O player."""
    up() # Lift the pen to move it without drawing
    goto(x + 67, y + 5) # Move the pen to the specified coordinates
    down() # Lower the pen to start drawing
    circle(62) # Draw a circle with radius 62


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0} # The dictionary that maintains the game state (who the current player is)
players = [drawx, drawo] # List of functions that draw the X's and O's, respectively


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x) # Rounds x coordinates to the nearest grid value
    y = floor(y) # Rounds y coordinates to the nearest grid value
    player = state['player'] # Gets the current player from the state
    draw = players[player] # Selects the player-based drawing function
    draw(x, y) # Draws the shape (X or O) at the selected position
    update() # Refreshes the screen
    state['player'] = not player # Switches to the next player


setup(420, 420, 370, 0) # Set the Turtle window to 420x420 pixels
hideturtle() # Hide the Turtle cursor
tracer(False) # Disable Turtle movement to prevent it from automatically drawing
grid() # Call the function to draw the grid
update() # Refresh the screen to show the changes
onscreenclick(tap) # Register the 'tap' function to run when the user clicks on the screen
done() # Terminate program execution
