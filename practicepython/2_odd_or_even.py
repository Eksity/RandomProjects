# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Extras:
#1: If the number is a multiple of 4, print out a different message.
#2: Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#main and extra #1
def is_even(number):
    if number % 4 == 0:
        print("Divisible by 4!")
    elif number % 2 == 0:
        print("Even!")
    else:
        print("Odd!")

# extra #2:
def is_divisible(num, check):
    if num % check == 0:
        print("Divisible!")
    else:
        print("Not divisible!")

def main():
    is_even(int(input("Check if even: ")))
    is_divisible(int(input("Check if: ")), int(input("is divisible by: ")))

if __name__ == "__main__":
    main()