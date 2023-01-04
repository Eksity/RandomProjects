def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#checks if every requirement is met
def is_valid(s):
    if correct_length(s) and correct_start(s) and correct_numbers(s) and only_letters_and_numbers(s):
        return True
    else:
        return False

#checks if the string length is between 2 and 6 inclusive
def correct_length(a):
    if len(list(a))>=2 and len(list(a))<=6:
        return True

    else:
        return False

#checks if the first two characters are numbers, if either one is returns False
def correct_start(b):
    for i in [0, 1]:
        if list(b)[i].isnumeric():
            return False
        else:
            return True

#checks every character in the string against every punctuation mark I could find on the keyboard
def only_letters_and_numbers(c):
    for i in range(len(list(c))):
        match list(c)[i]:
            case " "|","|"."|"/"|";"|":"|"<"|">"|"?"|"\""|"'"|"-"|"_"|"\\"|"|"|"!"|"@"|"#"|"$"|"%"|"^"|"&"|"*"|"("|")"|"+"|"=":
                return False
            case other:
                continue
    return True

#please don't be mad future me
#creates a list (numlist)
#for every character in the string, checks if it is a number
#if it's not a number, continues. if it (x) is a number, checks if the next one (y) is a number.
#if x is a number but y is not, returns false
#if both are numbers, adds x to numlist
#if there is no y, the program will throw an error so used a try/except to avoid that (excepts to continue)
#if all of the above checks out, checks if the first number in numlist is 0
#if above is true, returns False. If not, returns True. (used another try/except for if there are no numbers)
def correct_numbers(d):
    numlist = []
    for i in range(len(list(d))):
        if list(d)[i].isnumeric():
            numlist.append(list(d)[i])
            try:
                if list(d)[i+1].isnumeric():
                    continue
                else:
                    return False
            except:
                continue
        else:
            continue

    try:
        if numlist[0] == "0":
            return False
        else:
            return True
    except:
        return True




if __name__ == "__main__":
    main()