# ADDING ITEMS
#playerInventory = []
#while len(playerInventory) < 10:
    #item = input("What do you want to add?\n")
    #playerInventory.append(item) # .append() adds to END of the list.
#playerInventory.sort()
# .whatever() is known as a METHOD. It means "do this to that".
#print(playerInventory)

# REMOVE ITEMS
#while len(playerInventory) > 5:
    #item = input("What do you want to remove?\n")
    #playerInventory.remove(item)
#playerInventory.sort()
#print(playerInventory)

# FIXED INVENTORY SYSTEM
weaponList = [
    True, # sword
    False, # pistol
    True, # missile launcher
    False, # laser blaster
    False # ice beam
]
# each item/value in a list is an ELEMENT
# the location of each element in the list is the INDEX
# first element is index[0]
# stortcut to last element is index[-1]
#weaponNum = 0 
#while weaponNum < len(weaponList):
    #if weaponNum == 0 and weaponList[0] == True:
        #print("Your character is equipped with a shiny metal sword.\n")
    #if weaponNum == 0 and weaponList[1] == True:
       # print("Your character is equipped with a pistol.\n")
    #if weaponNum == 0 and weaponList[2] == True:
        #print("Your character is equipped with a missile launcher.\n")
    #if weaponNum == 0 and weaponList[3] == True:
        #print("Your character is equipped with a laser blaster.\n")
    #if weaponNum == 0 and weaponList[4] == True:
       # print("Your character is equipped with a ice beam.\n")
    #weaponNum += 1

# ITEM EXISTS IN INVENTORY
doorKeys = [
    "red",
    "blue",
    "green",
    "yellow"
]
item = input("Which key do you require?\n").lower().upper()
if item in doorKeys:
    print(f"You have the {item} key!\n")
else:
    print(f"You do not have the {item} key.\n")


# Random Enemy Generator