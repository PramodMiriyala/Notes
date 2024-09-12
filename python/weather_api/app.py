import requests
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key and default city from environment variables
api_key = os.getenv('API_KEY')  # Ensure your .env file has this key
city = os.getenv('CITY', 'London')  # Default to London if not set

app = FastAPI()

@app.get("/weather/{city_name}")
def get_weather(city_name: str = city):
    """Fetch weather data for a specified city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    print(url)  # Print the URL for debugging purposes

    # Make the API request
    response = requests.get(url, timeout=10)

    # Check if the response was successful
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    # Return the JSON response
    return response.json()

if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI application
    uvicorn.run(app, host="127.0.0.1", port=8000)