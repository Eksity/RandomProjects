#Ask the user for a string and print out whether this string is a palindrome or not.

def palindrome(str):
    reverse = ""
    for x in str:
        reverse = f"{x}{reverse}"
    if reverse == str:
        return True
    else:
        return False

def main():
    print(palindrome(input("Input: ")))

if __name__ == "__main__":
    main()