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

# i = 0
# while i < 50:
#     getRandomWord(wordList)
#     i += 1
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 