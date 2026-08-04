import requests

API_KEY='39a602c88ec4f1d75e6d6f2cfa04ae05'
city=str(input('Enter city name '))
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

response= requests.get(url)
data=response.json()
# print(data)
# print('\n')

# print(data['coord'])
print(data['rain'])
