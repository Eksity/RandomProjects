import sys
import os
import csv
#pip install tabulate
from tabulate import tabulate 
#features I'd like: 
#death save tracker (propably not too hard)

class Entity:
    def __init__(self, name, maxhealth, nowhealth, armor):
        self.name = name
        self.maxhealth = maxhealth
        self.nowhealth = nowhealth
        self.armor = armor
        self.order = 0

    def attr(self):
        return [self.name, self.maxhealth, self.nowhealth, self.armor, self.order]

    def damage(self, num):
        try:
            num = int(num)
        except ValueError:
            raise ValueError
        self.nowhealth -= num
    
    def heal(self, num):
        try:
            num = int(num)
        except ValueError:
            raise ValueError
        self.nowhealth += num

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, armor):
        if armor < 0:
            print('Invalid armor value, please try again')
            self.remove()
        self._armor = armor

    @property
    def nowhealth(self):
        return self._nowhealth

    @nowhealth.setter
    def nowhealth(self, nowhealth):
        if nowhealth <= 0:
            print(f"{self.name} is dead/dying! use \"remove {self.name}\" to remove them.")
        self._nowhealth = nowhealth

if __name__ == '__main__':
    combatants = []
    help = "remember everything is case sensitive!\navailable commands: damage | heal | add | remove\ndamage| syntax: damage name amount\nheal  | syntax: heal name amount\nadd   | syntax: add name\nremove| syntax: remove name\nend   | syntax: end"
    message = ''
    macfolder = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "dndtracker")
    winfolder = os.path.join(os.path.expanduser('~'), "AppData", "Local", "dndtracker")
    if sys.platform == 'darwin':
        if os.path.exists(macfolder):
            pass
        else:
            os.mkdir(macfolder)
        path = macfolder
    if sys.platform == 'win32':
        if os.path.exists(winfolder):
            pass
        else:
            os.mkdir(winfolder) 
        path = winfolder 
    while True:
        for x in combatants:
            x.order = combatants.index(x)
        if sys.platform == 'darwin':
            files = os.listdir(macfolder)
        if sys.platform == 'win32':
            files = os.listdir(winfolder)
        files = os.listdir(macfolder)
        filenames = []
        for x in files:
            if x[-4:] == ".csv":
                filenames.append(x[:-4])
        table = [['Name', 'Max HP', 'Current HP', 'AC']]
        for x in combatants:
            table.append(x.attr()[:-1])
        #os.system('cls' if os.name == 'nt' else 'clear')
        print(tabulate(table, headers="firstrow", tablefmt="heavy_grid"))
        person = 0
        if message:
            print(message)
        else:
            pass
        message = ''
        command = input('&: ').split(" ")
        match command[0]:
            case 'help' | 'h' | '-h':
                print(help)
            case 'end' | 'q' | 'quit':
                while True:
                    yn = input("Are you sure you want to end? this will delete all combat data. (y/n) ").lower()
                    if yn == 'y':
                        sys.exit('Combat ended by user')
                    elif yn == 'n':
                        break
                continue
            case 'damage':
                for x in combatants:
                    try:
                        if command[1] == x.attr()[0]:
                            try:
                                x.damage(command[2])
                                person = 1
                            except ValueError:
                                message = "Invalid command"
                    except IndexError:
                        message = "Invalid command"
                if person == 0:
                    message = 'combatant not found or command incomplete'
            case 'heal':
                person = 0
                for x in combatants:
                    try:
                        if command[1] == x.attr()[0]:
                            try:
                                x.heal(command[2])
                                person = 1
                            except ValueError:
                                message = "Invalid command"
                            except IndexError:
                                message = "Invalid command2"
                    except IndexError:
                        message = "Invalid command"
                if person == 0:
                    message = 'combatant not found or command incomplete'
            case 'remove':
                person = 0
                place = 0
                for x in combatants:
                    try:
                        if command[1] == x.attr()[0]:
                            del(combatants[place])
                            person = 1
                        else:
                            place += 1
                    except IndexError:
                        message = "Invalid command"
            case 'add':
                person = 0
                for x in combatants:
                    try:
                        if command[1] == x.attr()[0]:
                            person = 1
                    except IndexError:
                        message = "Invalid command"
                if person == 1:
                    message = "This combatant already exists"
                    continue
                try:
                    fighter = Entity(command[1], int(input('Max health: ')), int(input('Current health: ')), int(input('Armor Class: ')))
                except ValueError:
                    message = "Invalid command"
                    continue
                try:
                    combatants.insert(int(input("turn order (number): "))-1, fighter)
                except ValueError:
                    message = "Invalid order"
            case 'move':
                person = 0
                for x in combatants:
                    try:
                        if command[1] == x.attr()[0]:
                            try:
                                combatants.remove(x)
                                combatants.insert(int(command[2])-1, x)
                                person = 1
                            except ValueError:
                                message = "Invalid command"
                                person = 1
                            except IndexError:
                                message = "Invalid command2"
                                person = 1
                    except IndexError:
                        message = "Invalid command"
                if person == 0:
                    message = 'combatant not found or command incomplete'
            case 'save':
                name = f"{input('Save as: ')}.csv"
                if name in files:
                    no = False
                    while True:
                        yn = input(f"This will overwrite the existing encounter \"{name[:-4]}\". continue? (y/n): ")
                        if yn == 'y':
                            break
                        elif yn == 'n':
                            no = True
                            break
                        else:
                            continue
                    if no:
                        continue
                with open(f"{os.path.join(path, name)}", "w") as file:
                    writer = csv.writer(file)
                    for x in combatants:
                        writer.writerow(x.attr())
            case 'load':
                print("Current encounters: ")
                print(", ".join(filenames))
                name = input("Encounter to load: ")
                if name not in filenames:
                    message = "File not found"
                    continue
                else:
                    with open(f"{os.path.join(path, name)}.csv", "r") as file1:
                        reader = csv.reader(file1)
                        combatants = []
                        for row in reader:
                            fighter = Entity(row[0], int(row[1]), int(row[2]), int(row[3]))
                            combatants.insert(int(row[4]), fighter)
            case other:
                message = "Command not found, use \"help\" to see commands"