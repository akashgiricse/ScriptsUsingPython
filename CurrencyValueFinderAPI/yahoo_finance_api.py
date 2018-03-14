import json
from urllib.request import urlopen


with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()


data = json.loads(source)

# with open('yahoo_finance_api.json', 'w') as f:
#     json.dumps(data, f, indent=2)

# print(json.dumps(data, indent=2))

usd_rates = dict()
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price


print("Enter USD/<sortcut for the country's currency> for finding value of that currency in terms of 1 USD. ")
value = input()

print(usd_rates[value])
