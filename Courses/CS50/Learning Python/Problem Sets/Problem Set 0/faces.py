def convert(x):
    return x.replace(":)","🙂").replace(":(","🙁")

def main():
    print(convert(input("Convert this: ")))



main()