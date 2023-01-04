import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    test = re.match( r"([1-2]?[0-9]?[0-9]{1})\.([1-2]?[0-9]?[0-9]{1})\.([1-2]?[0-9]?[0-9]{1})\.([1-2]?[0-9]?[0-9]{1})", ip)
    if test:
        for group in test.group(1, 2, 3, 4):
            if int(group) <= 255:
                pass
            else:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()