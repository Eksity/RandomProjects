totalprice = 0.00
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

while 1==1:
    try:
        totalprice = totalprice + menu[input("Item: ").title()]
        print(f"Total: ${totalprice}0")
    except EOFError:
        break
    except KeyError:
        pass
