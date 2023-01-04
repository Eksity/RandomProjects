import sys
import csv
# pip install tabulate
from tabulate import tabulate

def arg_check(num):
    if len(sys.argv) != num:
        if len(sys.argv) < num:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv):
            sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a csv file")
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")


def make_table(filename):
    table = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append([row[0], row[1], row[2]])
    return table


def main():
    arg_check(2)
    print(tabulate(make_table(sys.argv[1]), headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()