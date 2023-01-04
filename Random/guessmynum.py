def guess(num, nlist):
    tr = input("Higher, Lower, or Correct? (h/l/c): ")
    match tr:
        case "h":
            nlist = [i for i in nlist if i > num]
            return (nlist[round(len(nlist)/2)], nlist)
        case "l":
            nlist = [i for i in nlist if i < num]
            return (nlist[round(len(nlist)/2)], nlist)
        case "c":
            return False

if __name__ == "__main__":
    numlist = [i for i in range(1, 101)]
    guessnum = numlist[round(len(numlist)/2)-1]
    tries = 0
    print(f"think of a number from 1 to {numlist[-1]}!")
    while True:
        print(f"My guess: {guessnum}")
        try:
            x = guess(guessnum, numlist)
            tries += 1
        except IndexError:
            tries = 0
            break
        if x:
            guessnum = x[0]
            numlist = x[1]
        elif not x:
            break
    if tries == 0:
        print("You cheated!")
    else:
        print(f"The number was {guessnum}, and I took {tries} tries!")