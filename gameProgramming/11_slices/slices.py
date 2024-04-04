# Slicing in Python

alphabet = 'abcdefghijklmnopqrstuvwxyz'
string0 = "Type a random string."
string1 = "Type another \# random string!"
string2 = "Why do I need @ these 3 random strings?"

# python treats strings like lists.
# there is an index value for each character in the string

print(alphabet[0]) # what letter prints? A
print(alphabet[-1]) # what letter prints? Z

# slice oprator :
# syntax stringName[start:stop]
# start = INCLUSIVE, slice will include that value
# stop = EXCLUSIVE, slice will STOP BEFORE this value

print(alphabet[4:12]) # what letters print? E L
# make a slice using one of your other strings. start 5, stop 11 print(alphabet[5:11]) F to K

# slice to the end
print(string1[8:]) # start from startValue, slice to end of string.

# slice from the start
print(string1[:23]) # start the beginning, stop 1 BEFORE stopValue.

# slice the whole thing
print(string2[:])
