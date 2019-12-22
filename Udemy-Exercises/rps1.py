print("Rock...Paper...Scissors")

p1 = input("P1, make your move: ")
p2 = input("P2, make your move: ")

if p1 == "rock" and p2 == "scissors":
    print("P2 wins!")
elif p1 == "rock" and p2 == "paper":
    print("P2 wins!")
elif p1 == "paper" and p2 == "scissors":
    print("p2 wins!")
elif p1 == "paper" and p2 == "rock":
    print("P1 wins!")
elif p1 == "scissors" and p2 == "paper":
    print("P1 wins!")
elif p1 == "scissors" and p2 == "rock":
    print("P1 wins!")
elif p1 == p2:
    print("It's a tie!")
else:
    print("something is wrong")
