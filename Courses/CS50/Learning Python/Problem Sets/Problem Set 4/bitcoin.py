#pip install requests
import requests
import sys
try:
    coin_num = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
bitindex = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
price = round(float(bitindex.json()["bpi"]["USD"]["rate_float"]) * coin_num, 4)
print(f"${price:,}")

