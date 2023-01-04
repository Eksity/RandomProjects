endString = ""
tweet = list(input("Input: "))
for i in range(len(tweet)):
    match tweet[i]:
        case "a"|"e"|"i"|"o"|"u"|"A"|"E"|"I"|"O"|"U":
            tweet[i] = ""
        case other:
            continue

for x in range(len(tweet)):
    endString = endString + tweet[x]

print(endString)
