#todo:
#Use \r (carriage return, see Countdown.py) and time.sleep() and some kind of terminal clear to keep all the games on the same row

# imports
import random

# rock paper scissors list
rps = ["rock", "paper", "scissors"]

#giving the computer a random choice
def randomguess(num):
    if num == 1:
        return rps[0]
    elif num == 2:
        return rps[1]
    elif num == 3:
        return rps[2]

# intro
print("Welcome to rock, paper, scissors!")
print("This game is best out of 3.")
begin = input("Enter 'y' to begin: ")

while 1==1:
    if begin != "y":
        begin = input("Enter 'y' to begin: ")
    else:
        break

# main play loop
def game():
    i=0
    # player and computer wins as global variables
    global playerwins
    playerwins = 0
    global computerwins
    computerwins = 0 

    # number of games
    global iterations 
    iterations = input("Enter the number of rounds: ")
    iterations = int(iterations)
    while i < iterations:
        playerguess = input("Enter your move in all lowercase (rock/paper/scissors): ")
        computerguess = randomguess(random.randrange(1,4))
        if playerguess == rps[0]:
            print("The computer chose " + computerguess)
            if computerguess == rps[0]:
                print("it's a tie! this one doesn't count.")
            elif computerguess == rps[1]:
                print("You lose!")
                i += 1
                computerwins += 1
            elif computerguess == rps[2]:
                print("You win!")
                i += 1
                playerwins += 1
        elif playerguess == rps[1]:
            print("The computer chose " + computerguess)
            if computerguess == rps[0]:
                print("You win!")
                i += 1
                playerwins += 1
            elif computerguess == rps[1]:
                print("it's a tie! this one doesn't count.")
            elif computerguess == rps[2]:
                print("You lose!")
                i += 1
                computerwins += 1
        elif playerguess == rps[2]:
            print("The computer chose " + computerguess)
            if computerguess == rps[0]:
                print("You lose!")
                i += 1
                computerwins += 1
            elif computerguess == rps[1]:
                print("You win!")
                i += 1
                playerwins += 1
            elif computerguess == rps[2]:
                print("it's a tie! this one doesn't count.")
        else:
            print("That's not a move!")
while 1==1:
    game()

    print("-------------------")   
    print("The game is over!")
    if playerwins > computerwins:
        print("You win! Great job!") 
        print("Your Score: %d/%d" % (playerwins, iterations))
    elif computerwins > playerwins:
        print("You lose! Better luck next time,")
        print("Your Score: %d/%d" % (playerwins, iterations))
    elif playerwins == computerwins:
        print("It's a tie! you won as much as you lost.")
        print("Your Score: %d/%d" % (playerwins, iterations))

    playagain = input("play again? (y/n) ")
    if playagain == "n":
        exit()
    elif playagain != "n" and playagain != "y":
        playagain = input("play again? (y/n) ")