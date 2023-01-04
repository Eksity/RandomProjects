grocery_list = []
final_dict = {}
while 1==1:
    try:
        grocery_list = grocery_list + [input("")]
    except EOFError:
        break

for item in sorted(grocery_list):
    if item not in final_dict:
        final_dict[item] = 1
    elif item in final_dict:
        final_dict[item] = final_dict[item] + 1

for x in final_dict:
    print(f"{final_dict[x]} {x.upper()}")