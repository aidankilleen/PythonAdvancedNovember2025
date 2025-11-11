# api_investigation.py

import requests


url = "https://api.acodingtutor.com/members/5?_delay=5000"
response = requests.get(url)

data = response.json()

print (data)

url = "https://api.acodingtutor.com/members/8?_delay=7000"
response = requests.get(url)

data = response.json()

print (data)

print ("Finished")

