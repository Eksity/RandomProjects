import re

def main():
    print(convert(input("Hours: ")))

def ampm(s):
    time = re.search(r"([0-1]?[0-9](?::[0-5][0-9])? (?:AM|PM)) to ([0-1]?[0-9](?::[0-5][0-9])? (?:AM|PM))",s)
    if time:
        for group in time.group(1, 2):
            if len(group) == 8:
                if int(group[0:2]) > 12:
                    raise ValueError
                else:
                    pass
        return time.group(1, 2)
    else:
        raise ValueError

def convert(x):
    p = ampm(x)
    times = []
    for time in p:
        if len(time) in [4, 5]:
            y = time.split(" ")
            y[0] = f"{y[0]}:00"
            time = f"{y[0]} {y[1]}"
        if time[-2] == "A" and len(time) == 7:
            h = time.split(":")
            time = f"0{h[0]}:{h[1][0:2]}"
            times.append(time)
        elif time[-2] == "A" and len(time) == 8:
            h = time.split(":")
            if int(h[0]) == 12:
                h[0] = "00"
            time = f"{h[0]}:{h[1][0:2]}"
            times.append(time)
        elif time[-2] == "P":
            z = time.split(":")
            z[0] = int(z[0]) + 12
            if int(z[0]) == 24:
                z[0] = "12"
            time = f"{z[0]}:{z[1][0:2]}"
            times.append(f"{time}")
    for time in times:
        if time[0:2] not in ["10", "11", "12"]:
            time = f"0{time}"
    return f"{times[0]} to {times[1]}"

if __name__ == "__main__":
    main()