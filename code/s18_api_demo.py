
import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

url = (f'https://api.openweathermap.org/data/2.5/weather?q=Boston&appid={API_KEY}$units=imperial')

# response = requests.get("https://oim.108122.xyz/words/random")

# print(response.json())

#response = requests.get(
    #"https://oim.108122.xyz/mass",
    #headers={"X-Token": "alejandroalejandro"},
#)
#data = response.json()

# print(data['name'])       # 'Massachusetts'
# print(data['governor'])   # 'Maura Healey'

#print(len(data))
#print(data.keys())

#towns = data["data"]
#print(type(towns))  # do this for explore the data structure

# pprint(towns)
# print(len(towns))
#pprint(towns[0])  # print the first town

#requests.post(
    #'https://oim.108122.xyz/message',
    #json={'message': 'Hello from Alejandro!'},
    #headers={'X-Token': 'alejandroalejandro'}
#)

