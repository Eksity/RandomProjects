from pyfiglet import Figlet
import random
import sys
figlet = Figlet()

if len(sys.argv) > 3 or len(sys.argv) == 2:
    sys.exit("Incorrect arguments")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit("Unknown Font")
    else:
        sys.exit("Incorrect Arguments")
elif len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
x = input("Input: ")
print(figlet.renderText(x))
