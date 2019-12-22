import random

list = ["rock", "paper", "scissors"]

p1 = input("Rock, paper, or scissors? ").lower()
choice = random.choice(list)

print("Computer plays: ", choice)

if p1 == choice:
    print("It's a tie.")
elif p1 == "rock":
    if choice == "paper":
        print("Computer wins.")
    elif choice == "scissors":
        print("You win!")
elif p1 == "paper":
    if choice == "scissors":
        print("Computer wins.")
    elif choice == "rock":
        print("You win!")
elif p1 == "scissors":
    if choice == "paper":
        print("You win!")
    elif choice == "rock":
        print("Computer wins.")
else:
    print("Something is wrong")

