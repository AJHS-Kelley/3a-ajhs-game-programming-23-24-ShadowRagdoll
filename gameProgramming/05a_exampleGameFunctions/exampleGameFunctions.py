# Example Game Functions, Lily King, v0.0
import random

# VARIABLE DELCARATIONS
numberSkill = 0 # Scale of 0 - 100, 100 being the best
listTypes = ["idk",
            "wah",
            "idem"]
otherStuff = None
what = None

def functionOne(numberSkill, listTypes):
    if numberSkill > 90 and listTypes == "idk" and otherStuff == "bit" and what == "?":
        sfk = random.randint(0, 100)
        if sfk > 10:
            print("Hit")
        else:
            print("Miss")
    elif numberSkill > 80 and listTypes == "idk" and otherStuff == "bit" and what == "ahh":
        sfk = random.randint(0, 100)
        if sfk > 50:
            print("Hit")
        else:
            print("Miss")
    else:
        print("end")

functionOne(95, "idk", "bit", "?")
functionOne(35, "idk", "bit", "ahh")

def coinFlip():
    coinFlip = random.ranint(1, 2)
    if coinFlip

def functionTwo():
    pass

def functionThree():
    pass

def functionFour():
    pass



