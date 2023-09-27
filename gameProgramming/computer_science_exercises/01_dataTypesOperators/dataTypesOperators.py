# Data Types and Operators, Lily King, v0.0

myInt = 5
myFloat = -3.0

# Arithmetic Operators -- PEMDAS
print(myInt + 25) # Addition
print(myFloat - 99) # Subtraction
print(myFloat * 15) # Muitiplication
print(myInt / 10) # Division
print(myInt ** 2) # Exponents

# Modulus -- divides, then returns remainder.
print(18 % 9)
# COMMONLY USED TO DETERMINE EVEN/ODD NUMBERS

# assignment operators
myString = "Blah blah blah"
x = 0
# = means "Assign the variable on the left the value on the right."
# = throws out any previously assigned value!

# Addition Assignment Operator
myString += " I need to buy some eggs."
x += 2
# += means "Keep the current value and add the new value from the right."

print(myString)
print(x)

# Comparison Operators -- Return True or False
print(6 > 7) # Greater Than
print(7 >= 6) # Greater than or equal to
print(5 < -3) # less then
print(-7 <= 5) # less then or equal to
print(3 == 9) # is equal to
print(0 != -4) # not equal to

# Logical Operators
# and requires ALL conditions to be True for overall True
print(7 > 2 and 4 < 10) # (True and True) == True
print(7 > 2 and 4 < 3) #(True and False) == False
print(7 > 2 and 4 > 3 and 1 != 2 and 5 == 5)

# or requires AT LEAST ONE condition to be True for overall True.
print(3 > 6 or 5 < 10) # (False or True) == True
print(-10 > -5 or 15 < 10) # (False or False) == False


# not -- 'opposite' value
favColor = "green"
print(favColor == not "blue")

print(4 > 3 and 1 != 2 and 5 < 3) 
# True and True and False 

