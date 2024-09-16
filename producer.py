from kafka import KafkaProducer
import json
import requests
import time
from api_key import API_KEY

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

# Kafka Producer to send data
def produce_weather_data():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    api_key =API_KEY
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

    while True:
        for city in cities:
            data = fetch_weather_data(api_key, city)
            producer.send('weather-data', data)
            print(f"Sent data for {city}")

        producer.flush()
        time.sleep(10) 

if __name__ == "__main__":
    produce_weather_data()
