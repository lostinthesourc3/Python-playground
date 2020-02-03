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
