import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
#Write API key
api_key = os.getenv("OPENWEATHER_API_KEY","HERE WRITE API KYE")

if not api_key:
    raise ValueError("API key not found! Please set it in a .env file.")

# List of famous Indian cities
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]
temperatures = []

# Fetch weather data for each city
for city in cities:
    try:
        complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        if data.get("cod") == 200:
            temperatures.append(data["main"]["temp"])
        else:
            print(f"Could not fetch data for {city}: {data.get('message', 'Unknown error')}")
            temperatures.append(None)
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")
        temperatures.append(None)

# Create a bar chart to visualize the temperatures
plt.figure(figsize=(8, 5))
bars = plt.bar(cities, temperatures, color='skyblue')

plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Different Cities in India")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Adding temperature labels on top of bars
for bar, temp in zip(bars, temperatures):
    if temp is not None:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{temp:.1f}°C",
                 ha="center", va="bottom", fontsize=10, color="black")

plt.show()
