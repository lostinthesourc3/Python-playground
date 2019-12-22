import random 

rand = random.randint(1,10)

while True: 
    guess = input("Pick and number from 1 to 10: ")
    guess = int(guess)
    if guess < rand: 
        print("TOO LOW")
    elif guess > rand:
        print("TOO HIGH")
    else:
        print("YOU WON!")
        play_again = input("Do you want to play again? y/n: ")
        if play_again == "y":
            rand = random.randint(1,10)
            guess = None 
        else: 
            print("Thanks for playing!")
            break
    