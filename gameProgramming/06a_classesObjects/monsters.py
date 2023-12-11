# Monsters, Lily King, v0.0


class Monster:
    def __init__(self, size, level, name):
        self.size = size
        self.level = level
        self.name = name
        self.experience = 50000

    def __str__(self):
        return f"Monster Name: {self.name}\nMonster Size: {self.size}\nMonster Level: {self.level}\nXP Value: {self.experience}\n"
        


myMonster = Monster("Big", 5, "Orc")
print(myMonster)

def actercy(self):
    print("You go for a attack")
    if self.size == "Big":
        print("You hit the monster.")
    else:
        print("You miss")
