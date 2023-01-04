def main():
    shorten(input("Input: "))


def shorten(word):
    endString = ""
    tweet = list(word)
    for i in range(len(tweet)):
        match tweet[i]:
            case "a"|"e"|"i"|"o"|"u"|"A"|"E"|"I"|"O"|"U":
                tweet[i] = ""
            case other:
                continue

    for x in range(len(tweet)):
        endString = endString + tweet[x]

    return endString


if __name__ == "__main__":
    main()