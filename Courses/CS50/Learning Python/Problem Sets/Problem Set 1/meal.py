def main():
    x = convert(input("What time is it? "))
    if x>=7.0 and x<=8.0:
        print("breakfast time")
    elif x>=12.0 and x<=13.0:
        print("lunch time")
    elif x>=18.0 and x<=19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    if time[-4:]=="a.m.":
        return int(time.rstrip("am. ").split(":",)[0]) + (int(time.rstrip("am. ").split(":",)[1])/60)
    elif time[-4:]=="p.m.":
        return (int(time.rstrip("pm. ").split(":",)[0]) + (int(time.rstrip("pm. ").split(":",)[1])/60))+12
    else:
        return int(time.split(":")[0]) + (int(time.split(":")[1])/60)

main()