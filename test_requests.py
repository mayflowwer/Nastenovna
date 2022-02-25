import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.get(BASE + 'pictures')

print(response.status_code)
# print(response.text)
print(response.json())

