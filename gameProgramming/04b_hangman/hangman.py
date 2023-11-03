import random
wordList =  'eggs bread toast beef cake blueberry candy butter apple noodles jam carrot potato beans steak dog cat fish bird rat bug bear mouse deer bunny ape racoon possum hippo cow'.split()
# .split() will split a string into separate elements, by default based on SPACE

# VARIABLE_NAMES that are ALL CAPS are CONSTANTS and not meant to change.
HANGMAN_BOARD = ['''
    +----+
         |
         |
         |
         |
       =====''','''   
    +----+
    O    |
         |
         |
         |
       =====''','''
    +----+
    O    |
    |    |
         |
         |
       =====''','''
    +----+
    O    |
   /|    |
         |
         |
       =====''','''
    +----+
    O    |
   /|\   |
         |
         |
       =====''','''
    +----+
    O    |
   /|\   |
   /     |
         |
       =====''','''
    +----+
    O    |
   /|\   |
   / \   |
         |
       =====''']

def getRandomWord(wordList):   
    wordIndex = random.randint(0 , len(wordList) - 1)
    # len(listName) - 1 IS THE MOST COMMON WAY TO PREVENT INDEX OUT OF RANGE ERRORS
    #print(wordIndex)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()
  
    # Display the missed letters
    print('Missed Letters:', end = ' ' )
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            # The : character is used to SLICE strings into pieces.
            # [i:] means slice from the start until index i.
            # [i+1:] means slice from i+1 until the END
            # [startingPoint:endingPoint]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
  # Only allow: single character, A-Z only, not guessed already.
  while True: # defult 'infinite' loop
    print('Guess a letter and press enter.')
    guess = input()
    guess = guess.lower() 
    if len(guess) != 1:
      print('Please enter a single letter.\n')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
      print('Please enter an English letter only.')
    elif guess in alreadyGuessed:
      print('Already guessed. Guess a different letter!')
  else:
     return guess

def playAgain():
   print('Do you want to play again? Yes or No, then press enter.')
   return input().lower().startswith('y') # return True/False based on input



# i = 0
# while i < 50:
#     getRandomWord(wordList)
#     i += 1
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 