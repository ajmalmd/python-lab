import random
try:
    randNum = random.randrange(1, 10)
    guess = int(input("Please guess a number between 1 and 9 and enter it: "))

    if guess == randNum:
        print("You've guessed right number")
    elif guess < randNum:
        print("You've guessed too low!")
    else:
        print("You've guessed too high!")
except:
    print("Number must be integer and between 1 & 9!!")
    quit()
