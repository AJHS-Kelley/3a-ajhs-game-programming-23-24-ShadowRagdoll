# function = A block of reusable code
#            place () after the function name to invoke it

def happyBirthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birth to you!")
    print()

happyBirthday("Dude", 20)



def displayInvoice(username, amount, dueDate):
    print(f"Hello {username}")
    print(f"Your bill of {amount:.2f} is due: {dueDate}")

displayInvoice("Lil", 42.50, "01/01")


# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z
def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


def createName(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

fullName = createName("lil", "king")

print(fullName)