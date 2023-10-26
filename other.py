firstChoice = ""
secChoice = ""
thirdChoice = ""
fouthChoice = ""
youReady = 0
print("Welcome to a normal day of life.\n")
print("You wake up in your room.\n")
firstChoice = input("Should you look around or leave for work?\n")
if input == "look around":
    print("You look around your room and see things like a hair brush, clothes, along with other things and you realize that you have to get ready and go to work.\n")
    print("So you get ready.\n")
    youReady += 1
    print("You now stand by your car.\n")
    secChoice = input("Should you look around or drive to work?\n")
    if input == "look around":
        print("You see that the neighors yard has a big box.\n")
        thirdChoice = input("Do you want to take it or leave it?\n")
        if input == "take it":
            print("You now have a box. What should you do with it?\n")
            fouthChoice = input("Make it your new table or make it your home?\n")
            if input == "make it your new table":
                print("You take it inside and")

        else:
            print("You now stand by your car.\n")
    else:
        if input == "drive to work" and youReady == 1:
            print("You when to work. Everything was a normal day.\n")
            print("Well, good job for just doing the bare minimum and not being stupid or being unlucky.\n")
            print("You made it though a single day in your life, good job.\n")
            print("Good ending")
        else:

else:
    if input == "leave for work":
        print("You now stand by your car.\n")
        secChoice = input("Should you look around or drive to work?\n")
    else: 
        print("Please type look around or leave for work for your selection.\n")
        firstChoice = input("Should you look around or leave for work?\n")





    

