import os
import csv
from datetime import datetime
import requests

FILENAME = "weather_logs.csv"
API_KEY = "ad532f5abc49fccbbd15717744daceb1"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature(C)", "Condition"])

def log_weather():
    city = input("Enter your city name: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    # Check if entry exists
    with open(FILENAME, "r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower():
                print("Entry for this city and date already exists!")
                return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("API Error:", data.get("message", "Unknown error"))
            return

        temp = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
        condition = data["weather"][0]["main"]

        # Append to CSV
        with open(FILENAME, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), round(temp, 2), condition])

        print(f"Logged weather for {city.title()} on {date}: {round(temp,2)}°C, {condition}")

    except Exception as e:
        print("Error:", e)

log_weather()


























