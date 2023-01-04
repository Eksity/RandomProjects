import json
import requests
import sys
from bs4 import BeautifulSoup
name = input("Name: ")
name = name.split(" ")
try:
    url = f'https://en.wikipedia.org/wiki/{name[0]}_{name[1]}'
except IndexError:
    url = f'https://en.wikipedia.org/wiki/{name}'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,'html.parser')
bday = soup.find(class_="bday")
bday = f"{bday}"[19:29]
if not bday:
    sys.exit("Person not found")
with open('info.json', 'r') as file:
    bdays = json.load(file)
bdays[' '.join(name)] = bday
with open('info.json', 'w') as file1:
    json.dump(bdays, file1)