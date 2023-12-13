import random

def rollDice(numRoll, sizeRoll):
    count = 0
    sum = 0
    while count < numRoll:
        roll = random.randint(1, sizeRoll)
        sum += roll
        count += 1
    return sum

def rollDicePrint(numRoll, sizeRoll):
    count = 0
    sum = 0
    while count < numRoll:
        roll = random.randint(1, sizeRoll)
        print(f"Roll #{count}: {roll}\n")
        sum += roll
        count += 1
    print(f"The sum is {sum}.\n")
    return sum

def isExploding(roll, sizeRoll):
    if roll == sizeRoll:
        isExploding = True
    else:
        isExploding = False
    return isExploding

def isDouble(roll1, roll2):
    if roll1 == roll2:
        isDouble = True
    else:
        isDouble = False
    return isDouble

roll1 = rollDice(1, 6)
roll2 = rollDice(1, 6)
print(f"roll1 is {roll1} and roll2 is {roll2}.")

if isDouble(roll1, roll2):
    print("It's a double!\n")
    
else:
    print("Womp womp. Not a double.\n")

