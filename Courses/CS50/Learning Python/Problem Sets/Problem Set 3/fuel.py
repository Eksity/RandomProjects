def get_percentage(per):
    try:
        return round((int(per[0])/int(per[1]))*100)
    except ZeroDivisionError:
        return "Fail"
    except ValueError:
        return "Fail"




def main():
    while 1==1:
        frac = input("Fraction: ").split("/")
        x = get_percentage(frac)
        if x == "Fail":
            pass
        elif x > 100:
            pass
        elif x >= 99:
            print("F")
            break
        elif x <= 1:
            print("E")
            break
        else:
            print(f"{x}%")
            break

main()