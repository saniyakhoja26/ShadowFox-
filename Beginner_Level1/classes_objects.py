"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: Classes and Objects
"""


# Avengers Class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)
        print()

    def is_leader(self):
        if self.name == "Captain America":
            print(self.name, "is the leader of the Avengers.\n")
        else:
            print(self.name, "is not the leader of the Avengers.\n")


# Creating Avenger objects
avenger1 = Avenger("Captain America", 100, "Male", "Super Strength", "Shield")
avenger2 = Avenger("Iron Man", 45, "Male", "Technology", "Armor")
avenger3 = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
avenger4 = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
avenger5 = Avenger("Thor", 1500, "Male", "Super Energy", "Mjolnir")
avenger6 = Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")

# Displaying information
avenger1.get_details()
avenger1.is_leader()

avenger2.get_details()
avenger2.is_leader()

avenger3.get_details()
avenger3.is_leader()

avenger4.get_details()
avenger4.is_leader()

avenger5.get_details()
avenger5.is_leader()

avenger6.get_details()
avenger6.is_leader()

print("\n---------------------------------------\n")
