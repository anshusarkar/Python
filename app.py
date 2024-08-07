#!/home/zero/miniconda3/envs/WeatherApp/bin/python

import requests
import os

# Replace with your actual API key

api_key = os.getenv("API_KEY")

# The key is saved in WSL ubuntu under WeatherAPP environment variable 


# Replace with the actual city name and country code
city_name = "San Francisco"
country_code = "US"

# API endpoint with parameters
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}"

# Make the GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.text)  # Print the error message returned by the API
