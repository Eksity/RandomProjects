#Make a two-player Rock-Paper-Scissors game.
def rps(a, b):
    if a == "rock":
        match b:
            case "rock":
                return "Tie"
            case "paper":
                return "P2"
            case "scissors":
                return "P1"
            case other:
                raise ValueError
    elif a == "paper":
        match b:
            case "rock":
                return "P1"
            case "paper":
                return "Tie"
            case "scissors":
                return "P2"
            case other:
                raise ValueError
    elif a == "scissors":
        match b:
            case "rock":
                return "P2"
            case "paper":
                return "P1"
            case "scissors":
                return "Tie"
            case other:
                raise ValueError

def main():
    while 1==1:
        print("Make your plays!")
        try:
            game = rps(input("Player 1: "), input("Player 2: "))
        except ValueError:
            print("Incorrect Input")
            continue
        if game == "P1":
            print("Player 1 wins!")
        elif game == "P2":
            print("Player 2 wins!")
        elif game == "Tie":
            print("It's a tie!")
        again = input("Play again? (y/n) ")
        if again == "y":
            continue
        else:
            break

if __name__ == "__main__":
    main()