choice = ("look around", "leave for work", "look around your room", "drive to work", "take it", "leave it", "make it your new table", "make it your home", "talk to them", "run")
youReady = 0
player = ""
running = True
while running:
    print("Welcome to a normal day of life.\n")
    print("You wake up in your room.\n")
    choice = input("Should you look around your room or leave for work?\n")
    while player not in choice:
        player = input("Please type exactly like one of the options above.")
        
    if player == "look around your room":
        print("You look around your room and see things like a hair brush, clothes, along with other things and you realize that you have to get ready and go to work.\n")
        print("So you get ready.\n")
        youReady += 1
        print("You now stand by your car.\n")
        choice = input("Should you look around or drive to work?\n")
        if choice == "look around":
            print("You see that the neighors yard has a big box.\n")
            choice = input("Do you want to take it or leave it?\n")
            if choice == "take it":
                print("You now have a box. What should you do with it?\n")
                choice = input("Make it your new table or make it your home?\n")
                if choice == "make it your new table":
                    print("You take it inside and make it your new table, but when you go back outside you see the neighbor giving you the scariness stare you have ever seen.\n")
                    print("A death stare, it looks like he might actually kill you.\n")
                    choice = input("should you talk to them or run?\n")
                    if choice == "run":
                        print("You run as fast as you can away from him.\n")
                        print("You look back as you are running to check to see if he is behind you.\n")
                        print("When you do this though you bump into another neighbor.\n")
                        print("She gives you the exact same kind of stare as the other neighbor.\n")
                        print("A death stare.\n")
                        print("Your Body Was Never Found Ending\n")
                    elif choice == "talk to them":
                            print("You go up to him to talk.\n")
                            print("He knows you took his box and he says that box meant a lot to him and how you just stole his property,\n")
                            print("You try to defend yourself, saying how you needed a table, but the thing is you had a table and you somehow forgot about it and placed the box over your table.\n")
                            print("As if you couldn't even see what your own living room looked like or something.\n")
                            print("The neighbor states that he is going to take you to court.\n")
                            print("That you are going to lose a lot of money and even if you don't it's still gonna be a huge inconvenience for you and be stressful.\n")
                            print("Court Issues Ending\n")
                    else:
                            print("Please type talk to them or run for your selection.\n")
                            choice = input("should you talk to them or run?\n")
                else:
                    if choice == "make it your home":
                        print("You decide that you don't want to work, ever again.\n")
                        print("All you had to do was go to work so you can get money for rent, but you gave up and decided to live in a box.\n")
                        print("At least it's rent free.\n")
                        print("Box Sweet Box Ending\n")
                    else:
                        print("Please type make it your new table or make it your home for your selection.\n")
                        choice = input("Make it your new table or make it your home?\n")
            else:
                print("You now stand by your car.\n")
        else:
            if choice == "drive to work" and youReady == 1:
                print("You when to work. Everything was a normal day.\n")
                print("Well, good job for just doing the bare minimum and not being stupid or being unlucky.\n")
                print("You made it though a single day in your life, good job.\n")
                print("Good ending")
            else:          
                if choice == "drive to work":
                    print("You when to work but you didn't get ready at all.\n")
                    print("Now it will probably be a funny story that will forever live in the office.\n")
                    print("The story of how someone managed to forget to get ready.\n")
                    print("Fired Ending\n")
    else:
        if choice == "leave for work":
            print("You now stand by your car.\n")
                
        