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

# A class is a 'blueprint' to make an object.

examplePerson = Person(6, "6'2\"", "black", "Pop", 70, "April 06")
examplePerson2 = Person(90, "6'2\"", "brown", "Bop", 170, "July 06")
print(examplePerson.name)
print(examplePerson.age)
print(examplePerson.height)

print(examplePerson2.name)
print(examplePerson2.hairColor)
print(examplePerson2.age)