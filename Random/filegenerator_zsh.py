#short script to create a bunch of files with random text in them to practice zsh commands
import random
import string
import sys

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
    inputs = []
    for line in sys.stdin:
        for f in line.split(" "):
            inputs.append(f)
    number = int(inputs[0])
    strrange = inputs[1]
    if strrange == "r":
        min = int(inputs[2])
        max = int(inputs[3])
        for z in range(number):
            charnumber = random.randint(min, max)
            makerandomfile(charnumber)
    elif strrange == "s":
        strlenght = int(inputs[2])
        for z in range(number):
            makerandomfile(strlenght)

main()

