import requests

url = 'http://localhost:5000/results'
r = requests.post(url, json = {'ENGINESIZE': 2, 'CYLINDERS': 4, 'FUELCONSUMPTION_CITY': 9.9, 'FUELCONSUMPTION_HWY': 6.7, 'FUELCONSUMPTION_COMB': 8.5})

print(r.json())