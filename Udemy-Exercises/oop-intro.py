# 1
class Vehicle:
    pass

car = Vehicle()
boat = Vehicle()

# 2
class Comment():
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

# 3
class BankAccount:
 
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance

# 4
class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

# 5
class Character():
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
 
    def speak(self):
        return "{0} says: 'I heard monsters running around last night!'".format(self.name)

# 6
class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"
 
 
class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"
 
 
class Child(Mother, Father):
    pass

#  7
class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars
 
    def __repr__(self):
        return "{} car train".format(self.num_cars)
 
    def __len__(self):
        return self.num_cars
