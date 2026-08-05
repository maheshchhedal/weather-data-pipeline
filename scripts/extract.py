import requests
import os
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CITIES = [
    "Kathmandu",
    "London",
    "Tokyo",
    "New York",
    "Sydney",
    "Paris",
    "Dubai",
    "Singapore",
    "Cairo",
    "Toronto"
]

API_KEY = os.getenv("WEATHER_API")
weather_records = []

for city in CITIES:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        response = requests.get(url)
        response_json = response.json()

        weather_record = {
            'city': response_json['name'],
            'country': response_json['sys']['country'],
            'latitude': response_json['coord']['lat'],
            'longitude': response_json['coord']['lon'],
            'temperature': response_json['main']['temp'],
            'temp_min': response_json['main']['temp_min'],
            'temp_max': response_json['main']['temp_max'],
            'humidity': response_json['main']['humidity'],
            'weather': response_json['weather'][0]['description'],
            'wind_speed': response_json['wind']['speed'],
            'visibility': response_json['visibility'],
            'timestamp': datetime.now()
        }
        weather_records.append(weather_record)

    except Exception as e:
        print(e)

# create dataframe
weather_df = pd.DataFrame(weather_records)
# print(weather_df)

exact_time = datetime.now().strftime('%Y%m%d_%H%M%S')

#save data into csv format 

weather_df.to_csv(f'data/incoming/weather{exact_time}.csv',index=False)