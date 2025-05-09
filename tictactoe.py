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
    color(purple)
    pensize(5)
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

def check_win(board, player_symbol):
    """Check if the player has won."""
    # Review rows and columns
    for i in range(3):
        if all(cell == player_symbol for cell in board[i]):
            return True
        if all(row[i] == player_symbol for row in board):
            return True
    # Check diagonals
    if all(board[i][i] == player_symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == player_symbol for i in range(3)):
        return True
    return False



state = {'player': 0} # The dictionary that maintains the game state (who the current player is)
board = [['' for _ in range(3)] for _ in range(3)]
players = [drawx, drawo] # List of functions that draw the X's and O's, respectively


def tap(x, y):
    """Draw X or O on the touched square and check for a win or draw."""
    x0 = floor(x)
    y0 = floor(y)

    # Convert graphic coordinates to board indices (row and column)
    col = int((x0 + 200) // 133)
    row = int((y0 + 200) // 133)

    # Validate if the box is already occupied
    if board[row][col] != '':
        return  # Ignore if there is already something in that box

    player = state['player']
    draw = players[player]
    draw(x0, y0)

    # Save symbol to logic board
    board[row][col] = 'X' if player == 0 else 'O'
    update()

    # Check if there is a winner
    if check_win(board, 'X'):
        print("¡Jugador X gana!")
        onscreenclick(None)  # Stop further clicks
        return
    elif check_win(board, 'O'):
        print("¡Jugador O gana!")
        onscreenclick(None)
        return
    # Check tie
    elif all(cell != '' for row in board for cell in row):
        print("¡Empate!")
        onscreenclick(None)
        return

    # Change shift
    state['player'] = not player



setup(420, 420, 370, 0) # Set the Turtle window to 420x420 pixels
hideturtle() # Hide the Turtle cursor
tracer(False) # Disable Turtle movement to prevent it from automatically drawing
grid() # Call the function to draw the grid
update() # Refresh the screen to show the changes
onscreenclick(tap) # Register the 'tap' function to run when the user clicks on the screen
done() # Terminate program execution
