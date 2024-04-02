# input the integers (A, B, C)
# .split() the integers into 3
# cast string to integers
# check for A < B < C

integers = input()
a, b, c = integers.split()
a = int(a)
b = int(b)
c = int(c)
if a > b:
    a, b = b, a # Extremely common method to swap values
elif c < b:
    c, b = b, c # Extremely common method to swap values
elif a > b:
    a, b = b, a
print(f"{a} {b} {c}")


# input the order
# create a string for output
# use a for loop to iterate the order -- What range?
    # if letter is A, add A integer + " " to string
    # if letter is B, add B integer + " " to string
    # if letter is C, add C integer + " " to string
# print the correct order to the screen.


