import random
while 1==1:
    level = input("Level: ").strip()
    try:
        level = int(level)
        if level > 0:
            break
        else:
            pass
    except ValueError:
        pass

try:
    number = random.randrange(1, level)
except ValueError:
    number = 1
    
while 1==1:
    guess = input("Guess: ").strip()
    try:
        guess = int(guess)
        if guess > level:
            pass
        elif guess == number:
            print("Just right!")
            break
        elif guess > number:
            print("Too Large!")
        elif guess < number:
            print("Too small!")
        else:
            pass
    except ValueError:
        pass