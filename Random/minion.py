#given a cost, run cost, reward, and cap how many runs will it take to make the original cost back?
#todo: 
#add output to read()
#add extra commands to read (list, help)
import csv
fieldnames = ["name", "cost", "runcost", "reward", "cap", "cycles"]

def cyclecheck(cost1, run1, reward1, cap1):
    cycles = 0
    current_cycle = 1
    current_value = cost1 * -1
    while cycles < 1000000:
        while current_value < cost1:
            if current_cycle < cap1:
                current_value = current_value - run1
                current_value = current_value + (reward1 * current_cycle)
                cycles += 1
                current_cycle += 1
            elif current_cycle == cap1:
                current_value = current_value - run1
                current_value = current_value + (reward1 * current_cycle)
                cycles += 1
        break
    return cycles


def make():
    with open("minions.csv", "a") as check:
        pass
    while 1==1:
        try:
            name = input("Name: ")
            cost = int(input("Original Cost: "))
            run = int(input("Run cost: "))
            reward = int(input("Reward: "))
            cap = int(input("Max level: "))
            cycles = cyclecheck(cost, run, reward, cap)
            minion = [cost, run, reward, cap, cycles]
            for attr in minion:
                if str(attr)[0] == "-":
                    print("No negative numbers")
                    raise ValueError
            minion.insert(0, name)
            with open("minions.csv", "r") as file1:
                reader1 = csv.DictReader(file1, fieldnames = fieldnames)
                for row in reader1:
                    if minion[0] == row["name"]:
                        print("Minion already exists")
                        raise ValueError
                    else:
                        pass
        except ValueError:
            print("Invalid input, please try again")
        else:
            break
    with open("minions.csv", "a") as file2: 
        writer = csv.DictWriter(file2, fieldnames = fieldnames)
        file2.seek(0, 2)
        writer.writerow({"name":minion[0], "cost":minion[1], "runcost":minion[2], "reward":minion[3], "cap":minion[4], "cycles":minion[5]})
    print(f"Minion \"{name}\" added!")

def read():
    while 1==1:
        findmin = input("Minion name: ")
        foundmin = []
        with open("minions.csv", "r") as file3:
            reader2 = csv.DictReader(file3, fieldnames = fieldnames)
            for row in reader2:
                if row["name"] == findmin:
                    for x in fieldnames:
                        foundmin.append(row[x])
                    break
                else:
                    pass
        #make sure foundmin has something in it
        if len(foundmin) == 6:
            print("\n")
            print("----- Minion Stats -----")
            print(f"Name: {foundmin[0]}")
            print(f"Original Cost: {foundmin[1]}")
            print(f"Cost per run: {foundmin[2]}")
            print(f"Reward per run: {foundmin[3]}")
            print(f"Cycles: {foundmin[4]}")

        else:
            while 1==1:
                s = input("Minion not found, try again? (y/n)").lower().strip()
                if s != "y" and s != "n":
                    continue
                else:
                    break
            if s == "y":
                continue
            elif s == "n":
                return
        break

        
def continuetest():
    pass    

def main():
    print("Welcome to Minion Maker!")
    while 1==1:
        x = input("Make or Read: ").strip().lower()
        if x == "make" :
            make()
        elif x == "read":
            read()
        else:
            continue
    
if __name__ == "__main__":
    main()