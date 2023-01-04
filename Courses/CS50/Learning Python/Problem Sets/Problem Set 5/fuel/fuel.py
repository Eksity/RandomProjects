def convert(fraction):
    try:
        fraction = fraction.split("/")
        if int(fraction[0])>int(fraction[1]) and fraction[1] != "0":
            raise ValueError
        return round((int(fraction[0])/int(fraction[1]))*100)
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError


def gauge(percentage):
        if percentage == ValueError:
            raise ValueError
        elif percentage == ZeroDivisionError:
            raise ZeroDivisionError
        elif percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
        elif 2 < percentage < 98:
            return f"{percentage}%"

def main():
    print(gauge(convert(input("Fraction: "))))

if __name__ == "__main__":
    main()