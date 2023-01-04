#qwerty output by 2: sygtva
def decipher(str, shift):
    alph = "abcdefghijklmnopqrstuvwxyz"
    shalph = f'{alph[int(shift):]}{alph[:int(shift)]}'
    output = ""
    for i in str:
        if i in alph:
            v = alph.find(i)
            output = f"{output}{shalph[v]}"
        else:
            output += i
    return output

def main():
    print(decipher(input("String: "), input("Shift: ")))

if __name__ == "__main__":
    main()