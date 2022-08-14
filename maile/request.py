import requests

x = requests.get('https://poczta.cyberfolks.pl')
print(x.status_code)