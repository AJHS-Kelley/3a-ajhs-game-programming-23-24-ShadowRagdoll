# project, Lily King, v0.0
#Code Reviewed By Eliot Blanton
import random

# variables
possibleGuess = 'even odd'.split()
#print(possibleGuess)
def randomNumber():
    randomNumber = random.randint(1, 2)

    return randomNumber

def getGuess(possibleGuess):
    while True:
        print("Even or odd?\n")
        guess = input()
        guess = guess.lower()
        #print("getGuessDEBUG")
        #print(guess)
        if guess not in possibleGuess:
            print("Please type in even or odd.\n")
        else:
            if guess == 'even': 
                guess = 2
            else: 
                guess = 1 
            return guess

def playAgain():
    print('Do you want to play again? Yes or No, then press enter.')
    playAgain = input().lower().startswith('y')    
    return playAgain
        
def didWin(guess, randomNumber):
    #print(f"guess type is {type(guess)}")
    #print(f"randomNumber type is {type(randomNumber)}")

    if guess == randomNumber: #try replacing randomNumber with a check for if the number being even/odd matches the guess
        print("You won a bunch of money!")
    else:
        guess != randomNumber
        print("You lost a bunch of money!")

# game start
print("Let's get a gambling addiction!\n")
print("You walk up to the roulette.\n")

while True:
    guess = getGuess(possibleGuess)
    # print(f"guess is {guess}")
    num = randomNumber()
    # print(f"num is {num}\n")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    didWin(guess, num)
    playMore = playAgain() 
    # print(f"playAgain is {playAgain}")
    if playMore == False: # Changed to break from the while True: if 'no' is entered.  
        break 
