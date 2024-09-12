"""__summary__"""
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
city_name = os.getenv('CITY')
api_key = os.getenv('API_KEY')
#http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric
Base_url = "http://api.openweathermap.org/data/2.5/"
Units = "units=metric"

response = requests.get(f"{Base_url}weather?q={city_name}&appid={api_key}&{Units}",
                        timeout=10)

if response.status_code == 200:
    data = response.json()
    print(data)
