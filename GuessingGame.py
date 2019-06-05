import random


guessNumber = random.randint(1,10)
while True:
    guess = int(input("Guesss a number betweeen 1 and 10: "))
    if  guessNumber > guess:
        print("Too, low, try again")
    elif guessNumber < guess:
        print("You are too high, try again")
    else:
        print("You won")
        print(guessNumber)
        exit = input("Do you want to play again (y/n): ")
        if exit == "y":
            guessNumber = random.randint(1,10)
            guess = None
        else:
            print("Thanks you for playing!")
            break
