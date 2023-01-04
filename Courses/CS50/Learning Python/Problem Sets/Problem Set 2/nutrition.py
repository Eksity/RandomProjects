item = input("Item: ").lower()

def findCal(x):
    match x:
        case "apple":
            return 130
        case "avocado"|"cantaloupe"|"honeydew melon"|"pineapple"|"strawberries"|"tangerine":
            return 50
        case "banana":
            return 110
        case "grapefruit"|"nectarine"|"peach":
            return 60
        case "grapes"|"kiwifruit":
            return 90
        case "lemon":
            return 15
        case "lime":
            return 20
        case "pear"|"sweet cherries":
            return 100
        case "plums":
            return 70
        case "watermelon"|"orange":
            return 80
        case other:
            return "Fail"

if findCal(item) == "Fail":
    pass
else:
    print("Calories: %i" % findCal(item))