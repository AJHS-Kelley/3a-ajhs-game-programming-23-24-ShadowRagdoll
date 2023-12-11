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