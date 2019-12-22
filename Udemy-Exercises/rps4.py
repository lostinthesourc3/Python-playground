import random

player_win = 0
comp_win = 0
winning_score = 3

while player_win < winning_score and comp_win < winning_score:
    list = ["rock", "paper", "scissors"]

    print(f"Player score: {player_win}. Computer score: {comp_win}")
    p1 = input("Rock, paper, or scissors? ").lower()
    choice = random.choice(list)

    print("Computer plays: ", choice)
    if p1 == "quit" or p1 == "q":
        break

    if p1 == choice:
        print("It's a tie.")
    elif p1 == "rock":
        if choice == "paper":
            print("Computer wins.")
            comp_win += 1
        elif choice == "scissors":
            print("You win!")
            player_win += 1
    elif p1 == "paper":
        if choice == "scissors":
            print("Computer wins.")
            comp_win += 1
        elif choice == "rock":
            print("You win!")
            player_win += 1
    elif p1 == "scissors":
        if choice == "paper":
            print("You win!")
            player_win += 1
        elif choice == "rock":
            print("Computer wins.")
            comp_win += 1
    else:
        print("Something is wrong")

if player_win > comp_win: 
    print("You win!")
elif player_win == comp_win:
    print("It's a tie")
else: 
    print("You lose!!!")
print(f"FINAL SCORES... Player: {player_win}. Computer: {comp_win}")