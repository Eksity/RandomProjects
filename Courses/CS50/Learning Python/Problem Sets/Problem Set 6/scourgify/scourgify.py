import sys
import csv

def arg_check(num):
    if len(sys.argv) != num:
        if len(sys.argv) < num:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv):
            sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
            sys.exit("Not a csv file")
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def convert(filename1, filename2):
    name_list = []
    first_name_list = ["first"]
    last_name_list = ["last"]
    house_list = ["house"]
    with open(filename1) as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            name_list.append(row["name"])
            house_list.append(row["house"])

    for name in name_list:
        name = name.split(",")
        first_name = f"{name[1].strip()}"
        last_name = f"{name[0]}"
        first_name_list.append(first_name)
        last_name_list.append(last_name)

    with open(filename2, "w") as file2:
        writer = csv.DictWriter(file2, fieldnames = ["first","last","house"])
        for name in range(len(first_name_list)):
            writer.writerow({"first":first_name_list[name], "last":last_name_list[name], "house":house_list[name]})

def main():
    arg_check(3)
    convert(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()