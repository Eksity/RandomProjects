def main():
    x = input("Greeting: ")
    print(f"${value()}")


def value(greeting):
    greeting = greeting.strip().lower()
    try:
        if greeting[0:5] == "hello":
            return 0
        elif greeting[0] == "h":
            return 20
        else:
            return 100
    except IndexError:
        return 100


if __name__ == "__main__":
    main()