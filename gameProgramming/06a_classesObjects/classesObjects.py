# Classes and Objects, Lily King, v0.0


class Person: # Class names should be PascalCase
    def __init__(self, age, height, hairColor, name, weight, birthday):
        # The self keyword refers to the specific object you are dealing with.
        self.age = age
        self.height = height
        self.hairColor = hairColor
        self.name = name
        self.weight = weight
        self.birthday = birthday

    # __str__ Method Format
    def __str__(self):
        return f"{self.name} is {self.age} years old. \nThey have {self.hairColor} hair and weigh {self.weight} pounds. \nThey were born on {self.birthday} and stands {self.height} tall."


# Functions In A Class
    def tooOld(self):
        print("Hello, this function will determine if you are too old to ride.\n")
        print("If you are older than 25 years, you cannot ride this ride.\n")
        if self.age > 25:
            print("You are too old, go find a different ride.\n")
        else:
            print("Welcome aboard!\n")

    def tooTall(self):
        print("Hello, this function will determine if you are too tall to ride.\n")
        print("If you are taller than 6.0, you cannot ride this ride.\n")
        if self.height == "6'2\"":
            print("You are too tall, go find a different ride.\n")
        else:
            print("Welcome aboard!\n")

# A class is a 'blueprint' to make an object.

examplePerson = Person(6, "6'2\"", "black", "Pop", 70, "April 06")
examplePerson2 = Person(90, "6'2\"", "brown", "Bop", 170, "July 06")

examplePerson.tooOld()
examplePerson2.tooOld()
examplePerson.tooTall()
examplePerson2.tooTall()
#print(examplePerson)

# Changing Properties After Creating Object
print(examplePerson.birthday)
examplePerson2.birthday = "June 27"
print(examplePerson2.birthday)



