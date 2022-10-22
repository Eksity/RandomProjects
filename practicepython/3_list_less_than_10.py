#Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
#Extras:
#1: Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#2: Write this in one line of Python.
#3: Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

#main and extras 1 and 2:
def less_than_5(list):
    return [num for num in list if num < 5]

#extra 3:
def less_than_given(list, check):
    return [num for num in list if num < check]

def main():
    print(a)
    print(less_than_5(a))
    print(less_than_given(a, input("Less than: ")))