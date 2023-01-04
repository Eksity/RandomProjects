month = ""
day = ""
year = ""
months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
    }
while 1==1:
    original = input("Date: ").strip()
    #format: month day, year
    if "," in original:
        original = original.split(" ")
        #month
        if original[0] in months:
            month = months[original[0]]
        else:
            month = "Fail"
        #day
        if len(original[1]) == 3:
            day = original[1][0:2]
        elif len(original[1]) == 2:
            day = f"0{original[1][0:1]}"
        else: day = "Fail"
        try:
            if int(day)>31:
                day = "Fail"
        except ValueError:
            day = "Fail"
        #year
        if len(original[2]) == 4:
            year = original[2]
        else:
            "Fail"
    #format: slashes
    elif "/" in original:
        original = original.split("/")
        #month
        try:
            if int(original[0]) <=12:
                if len(original[0]) == 1:
                    month = f"0{original[0]}"
                elif len(original[0]) == 2:
                    month = original[0]
                else:
                    month = "Fail"
            else:
                month = "Fail"
        except ValueError:
            month = "Fail"
        #day
        if int(original[1]) <=31:
            if len(original[1]) == 1:
                day = f"0{original[1]}"
            elif len(original[0]) == 2:
                day = original[1]
            else:
                day = "Fail"
        else:
            day = "Fail"
        #year
        if len(original[2]) == 4:
            year = original[2]
        else:
            year = "Fail"

    if month == "Fail" or day == "Fail" or year == "Fail":
        pass
    elif month == "" or day == "" or year == "":
        pass
    else:
        break
print(f"{year}-{month}-{day}")    