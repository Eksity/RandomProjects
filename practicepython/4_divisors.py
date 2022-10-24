#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

def all_divisors(num):
    divisor_list = []
    for number in range(num + 1)[1:]:
        if num % number == 0:
            divisor_list.append(number)
    return divisor_list

def main():
    print(all_divisors(int(input("Number: "))))

if __name__ == "__main__":
    main()