import sys

def arg_check(num):
    if len(sys.argv) != num:
        if len(sys.argv) < num:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv):
            sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a python file")
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")

def line_check(filename):
    line_count = 0
    with open(filename, "r") as file:
        for line in file:
            if line.strip() == "":
                pass
            elif line.strip()[0] == "#":
                pass
            else:
                line_count += 1

        return line_count

def main():
    arg_check(2)
    print(line_check(sys.argv[1]))

if __name__ == "__main__":
    main()