x = input("Expression: ").strip().split(" ")
if x[1] == "+":
    print(float(x[0]) + float(x[2]))
elif x[1] == "-":
    print(float(x[0]) - float(x[2]))
elif x[1] == "*":
    print(float(x[0]) * float(x[2]))
elif x[1] == "/":
    print(float(x[0]) / float(x[2]))