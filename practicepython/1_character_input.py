#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras:
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

def turn100(name, age, multiplier):
    print(multiplier * f"{name}, you will turn 100 in {2022 - age + 100}\n", end = "")

turn100(input("Name: "), int(input("Age: ")), int(input("Multiplier: ")))