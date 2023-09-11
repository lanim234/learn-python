import requests

x = requests.get('https://goal.com')

print(x.text)