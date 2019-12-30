# disctionaries exercises 

# 1
user_info = {"name": "Alice", "age": 25, "email": "alice@gmail.com"} 

# 2
artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]

# 3
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
 
for donation in donations.values():
    total_donations += donation

# 4
from random import choice 
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")

# 5
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

initial_game_state = dict.fromkeys(game_properties, 0)

# 6
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

stock_list = inventory.copy()
stock_list['cookie'] = 18
stock_list.pop('cake')