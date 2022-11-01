#short script to create a bunch of files with random text in them to practice zsh commands
from calendar import c
import random
import string

def strmaker(length):
    chars = []
    all = []
    output = ""
    for character in string.ascii_letters:
        all.append(character)
    for character1 in string.digits:
        all.append(character1)
    #for character2 in string.punctuation:
        #all.append(character2)
    for x in range(length):
        chars.append(random.choice(all))
    for y in chars:
        output = f"{output}{y}"
    return output

def makerandomfile(strlength):
    with open(f"{strmaker(5)}.txt", "w") as file:
        file.write(strmaker(strlength))

def main():
    while 1==1:
        try:
            number = int(input("How many files? "))
            strrange = input("Range of characters or set number? [r/s] ")
            if strrange != "r" and strrange != "s":
                print("Enter r for range or s for set number")
                raise ValueError
        except ValueError:
            print("Invalid input, please try again")
            continue
        else:
            break
    while 1==1:
        if strrange == "r":
                try:
                    min = int(input("Minimum amount of characters: "))
                    max = int(input("Maximum amount of characters: "))
                except ValueError:
                    print("Invalid input, please try again")
                    continue
                else:
                    for z in range(number):
                        charnumber = random.randint(min, max)
                        makerandomfile(charnumber)
                    break
        elif strrange == "s":
            try:
                strlenght = int(input("How many characters per file? "))
            except ValueError:
                print("Invalid input, please try again")
                continue
            else:
                for z in range(number):
                    makerandomfile(strlenght)
                break


    

if __name__ == "__main__":
    main()

