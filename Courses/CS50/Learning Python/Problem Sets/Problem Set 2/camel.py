endString = ""
camelCase = list(input("camelCase: ")) #t, e, s, t, I, n, p, u, t
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        camelCase[i] = "_"+camelCase[i].lower()

for x in range(len(camelCase)):
    endString = endString+camelCase[x]
print(endString)