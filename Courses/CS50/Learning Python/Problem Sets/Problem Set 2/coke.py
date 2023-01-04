amount_due = 50
while amount_due > 0:
    print("Amount Due: %i" % amount_due)
    amount_entered = input("Insert Coin: ")
    match amount_entered:
        case "5"|"10"|"25":
            amount_due = amount_due - int(amount_entered)
        case other:
            continue
print("Change Owed: %i" % (amount_due * -1))

