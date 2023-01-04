# importing random lib for number generation
import math
import random

# number of tries taken
tries = 0

# number to be guessed
win_number = str(math.floor(random.randrange(0, 100)))

# intro
print("Hello and welcome to Eksity's Guessing game!")
print("All you have to do is guess a number from 0-100.")
ready = input("ready? (y/n) ")

# main code
if ready == "n":
    print("Well, shucks.")
    exit()
elif ready == "y":
    print("Let's get going!")
    guess = input("Your guess: ")
    while 1==1:
        if guess == win_number:
            break
        else:
            if guess > win_number:
                print("Too high.")
                guess = input("Guess again: ")
            elif guess < win_number:
                print("Too low.")
                guess = input("Guess again: ")
            else:
                print("Something's not right.")
                guess = input("Guess again: ")
        tries = tries+1
else:
    print("That's not an answer!")

# outro
print("Correct! the number was " + win_number)
print(f"you took {tries} tries!")
print("Thanks for playing!")