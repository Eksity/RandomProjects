import re


def main():
    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r"((?:\b| )(?:u|U)m(?:\b| ))", s)
    umcount = 0
    for x in range(len(ums)):
        umcount += 1
    return umcount

if __name__ == "__main__":
    main()