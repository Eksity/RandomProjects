#Take two lists, say for example these two:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#Extras:
#1: Randomly generate two lists to test this (1-100 inc. in length, 1-100 inc. in values)
#2: Write this in one line of Python (no)

import random

#extra #1
def make_list(length, valuemin, valuemax):
    list = []
    for i in range(length + 1)[1:]:
        list.append(random.randint(valuemin, valuemax))
        
    return list

#main
def compare_lists(a, b):
    output = []
    for number in range(len(a)):
        if a[number] in b:
            if a[number] not in output:
                output.append(a[number])
    return output

def main():
    x = make_list(10, 1, 10)
    y = make_list(10, 1, 10)
    print(f"{x}\n{y}")
    print(compare_lists(x, y))

if __name__ == "__main__":
    main()