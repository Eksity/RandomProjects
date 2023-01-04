name_list = []
while 1==1:
    try:
        name_list = name_list + [input("Name: ")]
    except EOFError:
        break

if len(name_list) == 0:
    pass
elif len(name_list) == 1:
    print(f"Adieu, adieu, to {name_list[0]}")
elif len(name_list) == 2:
    print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")
else:
    ending = "Adieu, adieu, to "
    for name in range(len(name_list[:-1])):
        ending = ending + f"{name_list[name]}, "
    ending = ending + f"and {name_list[-1]}"
    print(ending)
