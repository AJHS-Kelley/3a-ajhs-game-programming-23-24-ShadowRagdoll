# Pick the secret number from a range for the possible numbers (i.e. 0-10, 0-100, 100-200)
# Provide the player X number of guesses, based on range of numbers.
# First player to score at least points is declared the winner.
    # Player guesses the number.
    # Compare guess to secret number.
    # If the guess is correct what should happen?
        # Award the player a point.
        # Print a 'win' message on the screen.
    # If the guess is incorrect, what should happen?
        # Indincate if guess is high/low compared to secret number.
    # If the player does not guess correctly before hitting limit, what happens?
        # Award a point to the CPU.
        # Print a loss message.
 

#Guess a Number, Lily King, v0.0
import random, tracemalloc, winsound
from PIL import Image
tracemalloc.start()

# DECLARATIONS
secretNumber = -1 # Range: 0 -- 20
playerName = "" # empty string
playerScore = 0
cpuScore = 0
numGuess = 0
playerGuess = -1 
gameDiff = ""
numAttempts = -1 
rangeMin = -1
rangeMax = -1 

loserSound = 'sfx/numberGuess/gameOver.wav'
winnerSound = 'sfx/numberGuess/win.wav'

imageWin = Image.open('img/numberGuess/win.png')
imageLoss = None

print("""
        +==============================+
        |                              |
        |       Guess the Number       |
        |              by              |
        |            Lily K.           |
        |             2023             |
        +==============================+
      """)

# diffcultly
gameDiff = input("How diffcult do you want?\nEasy has 5 attempts with 10 possiable numbers\nMidem has 5 attempts with 15 possiable numbers\nHard has 3 attempts with 20 possiable numbers\nType easy, midem, or hard.\n")
# This will work, but it is better to write it as an if-elif-else block.  The else: block should be a default value if the player does not pick correctly. 
if gameDiff == "easy": 
    numAttempts = 5
    rangeMin = 0
    rangeMax = 10
else:
    if gameDiff == "midem":
        numAttempts = 5
        rangeMin = 0
        rangeMax = 15
    else: 
        gameDiff == "hard"
        numAttempts = 3
        rangeMin = 0
        rangeMax = 20


playerName = input("What should I call you?\nType your name and press enter.\n")
# VERIFY INPUT WHENEVER POSSIBLE!
print(f"You want me to call you {playerName}. Is that correct?")
isCorrect = input("Please type yes if correct, no if not correct\n")
if isCorrect == "yes":
    print(f"Ok {playerName}, let's continue!")
else:
    playerName = input("What should I call you\nType your name and press enter.\n")

# GENERATE SECRET NUMBER -- You can delete lines 69-72.  You are generating the secret number in the loop now, you do not need this code anymore.  
# Change the next line to use variables instead of specific numbers. 
#secretNumber = random.randint(rangeMin, rangeMax) # INCLUSIVE
#print(secretNumber)

# PLAYER GUESSES
print(f"You need to guess a number from 0 to {rangeMax}. You have {numAttempts} guesses!\n")

while playerScore != 3 and cpuScore != 3: # match start
    #pass Tells Python to skip this block without giving an error.
    secretNumber = random.randint(rangeMin, rangeMax)
    print(secretNumber)
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}\n")
    numGuess = 0
    for guesses in range(numAttempts): # round start -- All players will get 4 guesses, what variable can you replace 4 with to change this based on difficulty? 

        print(f"You have {numAttempts - numGuess} guesses left this round!\n")
        playerGuess = int(input("Think of your number, type it in and then push ENTER.\n"))
        # int() converts whatever is input into an INTEGER
        print(f"You have picked {playerGuess}. Let's see if it is a match!\n")
        if playerGuess == secretNumber: 
            playerScore += 1
            print("A winner is you! It's a match!\n")
            winsound.PlaySound(winnerSound, winsound.SND_FILENAME)
            break # immediately exit a loop!
            #MOVE HERE
        else:
            if playerGuess < secretNumber:
                print("Your guess is too low!\n")
            else:
                print("Your guess is too high!\n")
        numGuess += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU was able to trick you and win this round!\n")
        winsound.PlaySound(loserSound, winsound.SND_FILENAME)

if playerScore >= 3:
    print("You have won three rounds, so you win the game!\n")
    imageWin.show()
else:
    print("Git gud scrub, the CPU was able to smash you!\n")
    imageLoss.show()

print("Memory Usage: (Current, Peak)")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()