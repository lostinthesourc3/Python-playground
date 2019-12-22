# SOME refactoring

print("Rock...Paper...Scissors")

p1 = input("P1, make your move: ")
p2 = input("P2, make your move: ")

if p1 == p2:
    print("It's a tie!")
elif p1 == "rock":
    if p2 == "scissors":
        print("P2 wins!")
    elif p2 == "paper":
        print("P2 wins!")
elif p1 == "paper":
    if p2 == "scissors":
        print("P2 wins!")
    elif p2 == "rock":
        print("P! wins!")
elif p1 == "scissors":
    if p2 == "rock":
        print("P1 wins!")
    elif p2 == "paper":
        print("P1 wins!")
else:
    print("something is wrong")
