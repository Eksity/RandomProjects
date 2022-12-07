#imports
import sys
import os
import csv
#pip install tabulate
try:
    from tabulate import tabulate 
except ModuleNotFoundError:
    sys.exit('"tabulate" module not found, please run "pip install tabulate" or your equivalent')

#create class for combatants
class Entity:
    def __init__(self, name, maxhealth, nowhealth, armor):
        self.name = name
        self.maxhealth = maxhealth
        self.nowhealth = nowhealth
        self.armor = armor
        self.order = 0
        self.kill = False

    def attr(self):
        return [self.name, f"{self.nowhealth}/{self.maxhealth}", self.armor, self.order]

    #method to subtract health
    def damage(self, num):
        try:
            num = int(num)
        except ValueError:
            raise ValueError
        self.nowhealth -= num
    
    #method to add health
    def heal(self, num):
        try:
            num = int(num)
        except ValueError:
            raise ValueError
        self.nowhealth += num

    @property
    def armor(self):
        return self._armor

    #make sure armor >= 0
    @armor.setter
    def armor(self, armor):
        if armor < 0:
            print('Armor class must be above zero')
            self.kill = True
        self._armor = armor

    @property
    def maxhealth(self):
        return self._maxhealth

    # make sure max health >= 1
    @maxhealth.setter
    def maxhealth(self, maxhealth):
        if maxhealth <= 0:
            print("Maximum health must be above zero")
            self.kill = True
        self._maxhealth = maxhealth

    @property
    def nowhealth(self):
        return self._nowhealth

    #add a message when a combatants' health drops below zero
    @nowhealth.setter
    def nowhealth(self, nowhealth):
        if nowhealth <= 0:
            print(f"{self.name} is dead/dying! use \"remove {self.name}\" to remove them.")
        self._nowhealth = nowhealth

if __name__ == '__main__':
    # declare constants
    combatants = []
    message = ''
    macfolder = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "dmhelper")
    winfolder = os.path.join(os.path.expanduser('~'), "AppData", "Local", "dmhelper")
    lnxfolder = os.path.join(os.path.expanduser('~'), ".local", "dmhelper")

    #create save folders and set save paths based on OS (ADD LINUX)
    if sys.platform.startswith('darwin'):
        if os.path.exists(macfolder):
            pass
        else:
            os.mkdir(macfolder)
        path = macfolder
    elif sys.platform.startswith('win32'):
        if os.path.exists(winfolder):
            pass
        else:
            os.mkdir(winfolder) 
        path = winfolder 
    elif sys.platform.startswith('linux'):
        if os.path.exists(lnxfolder):
            pass
        else:
            os.mkdir(lnxfolder) 
        path = lnxfolder

    #main usage loop
    while True:
        #set the combatants' order attribute in case anything changes
        for x in combatants:
            x.order = combatants.index(x)

        #set the files and filenames variables to the current file list in case anything changes
        if sys.platform.startswith('darwin'):
            files = os.listdir(macfolder)
        elif sys.platform.startswith('win32'):
            files = os.listdir(winfolder)
        elif sys.platform.startswith('linux'):
            files = os.listdir(lnxfolder)
        filenames = []

        #deal with extraneous files in the dmhelper folder
        for x in files:
            if x[-4:] == ".csv":
                filenames.append(x[:-4])

        #create output table
        table = [['Name', 'Health', 'AC']]
        for x in combatants:
            table.append(x.attr()[:-1])

        #clear terminal window
        os.system('cls' if sys.platform == 'win32' else 'clear')

        #print output
        print(tabulate(table, headers="firstrow", tablefmt="rounded_grid"))

        #print error message
        if message:
            print(message)
        else:
            pass

        #reset the message
        message = ''

        #wait for command from user
        command = input('&: ').split(" ")

        #do the command
        match command[0]:

            #kill the program
            case 'end' | 'q' | 'quit':
                while True:
                    yn = input("Are you sure you want to end? this will delete all unsaved combat data. (y/n) ").lower()
                    if yn == 'y':
                        sys.exit('Encounter ended by user')
                    elif yn == 'n':
                        break
                continue

            #damage a combatant using self.damage()
            case 'damage':
                try:
                    dname = command[1]
                except IndexError:
                    dname = input("Damage who? ")
                try:
                    dnum = command[2]
                except IndexError:
                    dnum = input("How much damage? ")
                for x in combatants:
                    try:
                        if dname == x.attr()[0]:
                            try:
                                x.damage(dnum)
                                person = 1
                            except ValueError:
                                message = "Invalid command"
                    except IndexError:
                        message = "Invalid command"
                if person == 0:
                    message = 'combatant not found or command incomplete'

            #heal a combatant using self.heal()
            case 'heal':
                try:
                    hname = command[1]
                except IndexError:
                    hname = input("Heal who? ")
                try:
                    hnum = command[2]
                except IndexError:
                    hnum = input("How much HP? ")
                person = 0
                for x in combatants:
                    try:
                        if hname == x.attr()[0]:
                            try:
                                x.heal(hnum)
                                person = 1
                            except ValueError:
                                message = "Invalid command"
                            except IndexError:
                                message = "Invalid command2"
                    except IndexError:
                        message = "Invalid command"
                if person == 0:
                    message = 'combatant not found or command incomplete'

            #remove a combatant by removing them from the list of combatants, therefore deleting all references to them.
            case 'remove':
                person = 0
                place = 0
                try:
                    rname = command[1]
                except IndexError:
                    rname = input("Who would you like to remove?")
                for x in combatants:
                    try:
                        if rname == x.attr()[0]:
                            del(combatants[place])
                            person = 1
                        else:
                            place += 1
                    except IndexError:
                        message = "Invalid command"

            #add a new Entity object to the combatants list
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
                if fighter.kill:
                    continue
                try:
                    combatants.insert(int(input("turn order (number): "))-1, fighter)
                except ValueError:
                    message = "Invalid order"

            #change a combatant's place in the list
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

            #save the current encounter to a csv file
            case 'save':
                try:
                    senc = f"{command[1]}.csv"
                except IndexError:
                    senc = f"{input('Save as: ')}.csv"
                if senc in files:
                    no = False
                    while True:
                        yn = input(f"This will overwrite the existing encounter \"{senc[:-4]}\". continue? (y/n): ").lower()
                        if yn == 'y':
                            break
                        elif yn == 'n':
                            no = True
                            break
                        else:
                            continue
                    if no:
                        continue
                with open(f"{os.path.join(path, senc)}", "w") as file:
                    writer = csv.writer(file)
                    for x in combatants:
                        writer.writerow(x.attr())

            #load an existing encounter from a csv file
            case 'load':
                try:
                    enc = command[1]
                except IndexError:
                    print("Current encounters: ")
                    print(", ".join(filenames))
                    enc = input("Encounter to load: ")
                if enc not in filenames:
                    message = "File not found"
                    continue
                else:
                    with open(f"{os.path.join(path, enc)}.csv", "r") as file1:
                        reader = csv.reader(file1)
                        combatants = []
                        for row in reader:
                            if row:
                                combatant = Entity(row[0], int(row[1].split("/")[1]), int(row[1].split("/")[0]), int(row[2]))
                                combatants.insert(int(row[3]), combatant)
            
            #if none of the above are used, give an error.
            case other:
                message = "Command not found, use \"help\" to see commands"