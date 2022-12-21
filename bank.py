# for any transaction over 1000, enter it into a special table called "flags"

#imports
import sqlite3
import os
import sys
import random
from tabulate import tabulate

#filepaths
macfolder = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "Eksity", "Bank")
winfolder = os.path.join(os.path.expanduser('~'), "AppData", "Local", "Eksity", "Bank")
lnxfolder = os.path.join(os.path.expanduser('~'), ".local", "Eksity", "Bank")

#SQLite setup
#connect to bank .db file
if sys.platform.startswith('darwin'):
    if os.path.exists(macfolder):
        pass
    else:
        os.makedirs(macfolder)
    path = macfolder
elif sys.platform.startswith('win32'):
    if os.path.exists(winfolder):
        pass
    else:
        os.makedirs(winfolder) 
    path = winfolder 
elif sys.platform.startswith('linux'):
    if os.path.exists(lnxfolder):
        pass
    else:
        os.makedirs(lnxfolder) 
    path = lnxfolder
con = sqlite3.connect(os.path.join(path, "bank.db"))
cur = con.cursor()
#user-inaccessible list of accounts
accounts = []

#create account list
def accountlist():
    l = cur.execute("SELECT accnum FROM accounts")
    for x in l:
        accounts.append(x[0])

# password checker
def pwdcheck(acc):
    pwdcheck = cur.execute(f"SELECT accpwd FROM accounts WHERE accnum = '{acc}';").fetchall()[0][0]
    inc = 0
    while True:
        if inc == 3:
            sys.exit("Too many invalid attempts")
        pwd = input("Password: ")
        if pwd != pwdcheck:
            inc += 1
            print("Incorrect Password")
            continue
        elif pwd == pwdcheck:
            break

# account number checker
def acccheck(acc):
    if acc not in accounts:
        raise ValueError("Account not found")

# flag transactions
def flagcheck(acc1, acc2, amt):
    if int(amt) > 1000:
        if acc1 and acc2:
            cur.execute(f"INSERT INTO flags VALUES('{acc1}', '{acc2}', {int(amt)}")
        elif acc1 and not acc2:
            cur.execute(f"INSERT INTO flags('from', 'amt') VALUES({acc1}, {amt})")
        elif acc2 and not acc1:
            cur.execute(f"INSERT INTO flags('to', 'amt') VALUES({acc2}, {amt})")
        con.commit()


# in-account loop
def interface(logac):
    message = ''
    while True:
        # get balance
        bal = int(cur.execute(f"SELECT balance FROM '{logac}'").fetchall()[-1][0])

        #clear terminal for gui feel
        os.system('cls' if sys.platform == 'win32' else 'clear')
        if message: print(message)
        message = ''
        print(f"Current balance: {bal}")
        cmd = input(f"{logacc}: ").split(" ")
        match cmd[0]:

            case 'list':
                table = [["ID", "Type", "Amount", "Balance"]]
                values = cur.execute(f"SELECT * FROM '{logac}'").fetchall()
                for x in values:
                    table.append(x)
                message = tabulate(table, headers="firstrow", tablefmt="rounded_grid")

            case 'deposit':
                try:
                    amt = int(cmd[1])
                except ValueError:
                    message = "Invalid amount"
                    continue
                except IndexError:
                    try:
                        amt = int(input("Amount: "))
                    except ValueError:
                        message = "Invalid amount"
                        continue
                bal += amt
                flagcheck(False, logacc, amt)
                cur.execute(f"INSERT INTO '{logac}'(type, amount, balance) VALUES('Deposit', {amt}, {bal});")
                p = cur.execute(f"SELECT * FROM accounts WHERE accnum = '{logac}';").fetchall()[0][1]
                cur.execute(f"DELETE FROM accounts WHERE accnum = '{logac}';")
                cur.execute(f"INSERT INTO accounts VALUES('{logac}', '{p}', '{bal}')")
                cur.execute(f"INSERT INTO logs VALUES('0000000000', '{logac}', {amt});")
                con.commit()
                message = f"Successfully deposited {amt}"

            case 'withdraw':
                try:
                    amt = int(cmd[1])
                except ValueError:
                    message = "Invalid amount"
                    continue
                except IndexError:
                    try:
                        amt = int(input("Amount: "))
                    except ValueError:
                        message = "Invalid amount"
                        continue
                bal -= amt
                flagcheck(logacc, False, amt)
                cur.execute(f"INSERT INTO '{logac}'(type, amount, balance) VALUES('Withdrawal', {amt}, {bal});")
                p = cur.execute(f"SELECT * FROM accounts WHERE accnum = '{logac}';").fetchall()[0][1]
                cur.execute(f"DELETE FROM accounts WHERE accnum = '{logac}';")
                cur.execute(f"INSERT INTO accounts VALUES('{logac}', '{p}', '{bal}')")
                cur.execute(f"INSERT INTO logs VALUES('{logac}', '0000000000', {amt});")
                con.commit()
                message = f"Successfully withdrew {amt}"

            case 'transfer':
                try:
                    other = cmd[1]
                except IndexError:
                    other = input("Transfer to account #")
                try:
                    acccheck(other)
                except ValueError:
                    message = "Account not found"
                    continue
                try:
                    tramt = int(cmd[2])
                except ValueError:
                    message = "Invalid Amount"
                    continue
                except IndexError:
                    try:
                        tramt = int(input("Amount to transfer: "))
                    except ValueError:
                        message = "Invalid Amount"
                        continue
                if tramt <= 0:
                    message = "Transfer only available for amounts above 0"
                    continue
                altbal = int(cur.execute(f"SELECT balance FROM '{other}'").fetchall()[-1][0])
                bal -= tramt
                altbal += tramt
                flagcheck(logacc, other, tramt)
                cur.execute(f"INSERT INTO '{logac}'(type, amount, balance) VALUES('WTransfer', {tramt}, {bal});")
                cur.execute(f"INSERT INTO '{other}'(type, amount, balance) VALUES('DTransfer', {tramt}, {altbal});")
                p = cur.execute(f"SELECT * FROM accounts WHERE accnum = '{logac}';").fetchall()[0][1]
                op = cur.execute(f"SELECT * FROM accounts WHERE accnum = '{other}';").fetchall()[0][1]
                cur.execute(f"DELETE FROM accounts WHERE accnum = '{logac}';")
                cur.execute(f"INSERT INTO accounts VALUES('{logac}', '{p}', '{bal}');")
                cur.execute(f"DELETE FROM accounts WHERE accnum = '{other}';")
                cur.execute(f"INSERT INTO accounts VALUES('{other}', '{op}', '{altbal}');")
                cur.execute(f"INSERT INTO logs VALUES('{logac}', '{other}', {tramt});")
                con.commit()
                message = f"Successful transfer to {other}: {tramt}"
            
            case 'logout':
                while True:
                    yn = input("Logout? (y/n) ")
                    if yn == 'y':
                        os.system('cls' if sys.platform == 'win32' else 'clear')
                        sys.exit("Successfully logged out.")
                    elif yn == 'n':
                        break
                    else:
                        continue
                continue

# main function
if __name__ == "__main__":
    cur.execute("CREATE TABLE IF NOT EXISTS accounts(accnum TEXT, accpwd TEXT, balance TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS flags('from' TEXT, 'to' TEXT, 'amt' INTEGER);")
    cur.execute("CREATE TABLE IF NOT EXISTS logs('from' TEXT, 'to' TEXT, 'amt' INTEGER);")
    try:
        assert sys.argv[1] == sys.argv[1]
    except IndexError:
        sys.exit("Please include command")
    accountlist()

    match sys.argv[1]:
        case 'create':
            pwd = input("Password: ")
            pwd2 = input("Confirm password: ")
            if pwd != pwd2:
                sys.exit("Passwords did not match")
            try:
                mon = int(input("Starting amount: "))
            except ValueError:
                sys.exit("Invalid starting amount")
            while True:
                num = str(random.randrange(1000000000, 9999999999))
                if num not in accounts:
                    break
                else:
                    continue
            cur.execute(f"CREATE TABLE '{num}'(id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, amount INTEGER, balance INTEGER);")
            cur.execute(f"INSERT INTO '{num}'(type, amount, balance) VALUES('Deposit', {mon}, {mon});")
            cur.execute(f"INSERT INTO logs VALUES('0000000000', '{num}', '{mon}');")
            cur.execute(f"INSERT INTO accounts VALUES('{num}', '{pwd}', '{mon}');")
            con.commit()
            print(f"Account created! Your account number is {num}, please remember it!")

        case 'delete':
            try:
                num = sys.argv[2]
            except IndexError:
                try:
                    num = int(input("Account number: "))
                    num = str(num)
                except ValueError:
                    sys.exit("Invalid account number")
            if num not in accounts:
                sys.exit("Invalid account number")
            pwdcheck(num)
            while True:
                yn = input(f"Are you sure you want to delete account #{num}? (y/n): ")
                if yn == 'y':
                    break
                elif yn == 'n':
                    sys.exit("Account deletion canceled by user")
            cur.execute(f"DROP TABLE '{num}';")
            cur.execute(f"DELETE FROM accounts WHERE accnum = '{num}';")
            con.commit()
            print("Account Deleted!")

        case 'login':
            logacc = input("Account number: ")
            try:
                acccheck(logacc)
            except ValueError:
                sys.exit("Account not found")
            pwdcheck(logacc)
            interface(logacc)

        
        case other:
            sys.exit("Invalid command")

    cur.close()
    con.close()