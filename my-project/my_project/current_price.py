import requests

URL = "https://api.coinbase.com/v2/prices/spot?currency=USD"
resp = requests.get(URL).json()

data = resp['data']
print("{}: ${}".format(data['base'], data['amount']))
