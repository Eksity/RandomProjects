import json
from collections import Counter
import os
lis = []
months = {
    "01":"January",
    "02":"February",
    "03":"March",
    "04":"April",
    "05":"May",
    "06":"June",
    "07":"July",
    "08":"August",
    "09":"September",
    "10":"October",
    "11":"November",
    "12":"December"
}
with open(os.path.join(os.path.expanduser('~'), "Desktop", "Code", "Python","Courses", "practicepython", "bdaydata", "info.json"), 'r') as file:
    x = dict.values(json.load(file))
for y in x: 
    z = y.split("-")
    lis.append(months[z[1]])

c = Counter(lis)
for x in months:
    if months[x] in c:
        print(f"{months[x]}: {c[months[x]]}")
