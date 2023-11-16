# project, Lily King, v0.0
import random

# variables
possibleGuess = 'even odd'.split

def getGuess():
    while True:
        print("Even or odd?\n")
        guess = input()
        guess = guess.lower
        if guess != "even" or "odd":
            print("Please type in even or odd.\n")
        else:
            return guess


print("Let's get a gambling addiction!\n")
print("You walk up to the roulette.\n")
print("Even or odd?\n")
