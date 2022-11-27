import sys
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

    def attr(self):
        return [self.name, self.maxhealth, self.nowhealth, self.armor]

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
    help = "remember everything is case sensetive!\navailable commands: damage | heal | add | remove\ndamage| syntax: damage name amount\nheal  | syntax: heal name amount\nadd   | syntax: add name\nremove| syntax: remove name\nend   | syntax: end"
    message = ''
    while True:
        table = [['Name', 'Max HP', 'Current HP', 'AC']]
        for x in combatants:
            table.append(x.attr())
        print(tabulate(table, headers="firstrow", tablefmt="heavy_grid"))
        #todo: clear terminal
        #todo: display info
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
                try:
                    fighter = Entity(command[1], int(input('Max health: ')), int(input('Current health: ')), int(input('Armor Class: ')))
                except ValueError:
                    message = "Invalid command"
                    continue
                try:
                    combatants.insert(int(input("turn order (number): "))-1, fighter)
                except ValueError:
                    message = "Invalid order"
            case other:
                message = "Command not found, use \"help\" to see commands"