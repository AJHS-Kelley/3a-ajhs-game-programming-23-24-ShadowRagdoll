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
