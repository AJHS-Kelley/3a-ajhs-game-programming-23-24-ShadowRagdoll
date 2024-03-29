# Number Slide Game, Lily King, based on project by AI Sweigart, v0.0

# GAME SETUP / STEPS 
# Function to layout / setup the grid.
# Create the tiles and add to board.
# Check for Valid Movements.
# Animate movement of tile.
# Allow for user input to select tile (mouse click)
# Identify location coordinates of mouse click, determine tile selected
# Check for win -- All numbers in correct order.

# DIVIDE AND CONQUER METHOD -- Break down a larger problem into smaller problems, then solve those.

# MODULE IMPORTS
import pygame, sys, random, time
# sys module gives access to system level functions including open/close programs, etc.

# MODULE IMPORTS -- specific functions!
from pygame.locals import *
# this line allows us to call functions directly instead of pygame.function()
# we can just write function()
# * in this line is a WILDCARD and means any or all.
# Example: delete myGameFiles*


# BOARD SETUP DATA
BOARDWIDTH = 4 # COLUMNS
BOARDHEIGHT = 4 # ROWS

# TILE DATA
TILESIZE = 80 # MEASURED IN PIXELS

# WINDOW SIZE
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS

# FRAMES PER SECOND
FPS = 30 # SETS MAXIMUM, DOES NOT 'IMPROVE PERFORMANCE' ON A POTATO

# BLANK TILE VALUE
BLANK = None


# COLOR VALUES = (R, G, B)
# Min. Value = 0, Max. Value = 255, think of drops of food coloring.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# ASSIGN COLORS TO GAME OBJECTS
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE

# FONT SIZE
BASICFONTSIZE = 20 # MEASURED IN PIXELS

# BUTTON AND MESSAGES
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE 

# MARGINS FOR WINDOW
XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH -1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT -1))) / 2)

# DIRECTIONAL ASSIGNMENTS
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Main Game Loop
def main():
    # global keyword makes Python use the same variable in entire program.
    global FPSCLOCK, DISPLAYSURF, BASIC_FONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
    # SURF IS THE ABBREVIATON FOR 'SURFACE'
    # A 'SURFACE' IN PYGAME CAN BE USED TO DRAW GRAPHICS, TEXT, OR SIMPLE COLORS.
    # THE EASY WAY TO THINK OF THE 'SURFACE' IS A WHITEBOARD.

    # RECT IS THE ABBREVIATION FOR RECTANGLE

    # START THE PYGAME MODULE ITSELF! THIS LINE OF CODE IS REQUIED FOR PYGAME TO WORK!

    pygame.init() # Start the PyGame Module
    FPSLOCK = pygame.time.Clock() # Establish the 'start' to track FPS
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # CREATE the game window.
    pygame.display.set_caption('Lily\'s Slip Slide')
    time.sleep(5)


# End the game
def terminate() -> None:
    pygame.quit() # this will 'end' all the pygame events, etc.
    sys.exit() # Quit the program using the Operating System Commands.

# Check if the Player Quits
def checkForQuit() -> None:
    for event in pygame.event.get(QUIT):
        terminate() # Terminate the game if a QUIT event is present.
    for event in pygame.event.get(KEYUP): # Triggers when the specific key is RELEASED.
        if event.key == K_ESCAPE: # Trigger if ESC is RELEASED.
            terminate()
        pygame.event.post(event) # Put the other events back into the stack of dishes (queue)

def getLeftTopOfTile(tileX: int, tileY: int) -> tuple:
    left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
    top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
    return (top, left)
    
def getSpotClick(board: list, x: int, y: int) -> tuple:
    for tileX in range(len(board)): # Loop through every tile on x-axis ONCE.
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY) # Tell us where the tile is.
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            # pygame.Rect(left, top, width, height)
            if tileRect.collidepoint(x, y): # Does our object hit something at (x, y)?
            # .collidepoint() is basically Battleship.
                return (tileX, tileY) # If we 'hit' return the location.
    return (None, None) # If we 'miss' return None, None.


    return (None, None)


main()