# project, Lily King, v0.0
import random

# variables
possibleGuess = 'even odd'.split

def randomNumber():
    randomNumber = random.randint(1, 36)

def getGuess():
    while True:
        print("Even or odd?\n")
        guess = input()
        guess = guess.lower
        if guess != possibleGuess:
            print("Please type in even or odd.\n")
        else:
            return guess

def playAgain():
    print('Do you want to play again? Yes or No, then press enter.')
    return input().lower().startswith('y') # return True/False based on input

def didWin():
    if guess == randomNumber:
        print("You won a bunch of money!")
    else:
        guess != randomNumber
        print("You lost a bunch of money!")

# game start
print("Let's get a gambling addiction!\n")
print("You walk up to the roulette.\n")
while True:
    guess = getGuess()
    randomNumber()
    if randomNumber % 2 == 0:
        print("Even")
    else:
        print("Odd")
    didWin()
    playAgain()