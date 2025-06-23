"""
Create a CSV file for address book, CSV file have columns for name, address, mobile,
email. Insert 2-3 dummy data
"""

import csv

data = [['Name', 'Address', 'Mobile', 'Email'],
        ['Amit', 'Model Town, Jaipur', '66652346', 'amit@gmail.com'],
        ['Bhumi', 'Malviya Nagar, Jaipur', '65555556', 'bhumi@gmail.com'],
        ['Diya', 'Bajaj Nagar, Jaipur', '56666666', 'diya@gmail.com']
        ]

with open('addresses.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)

with open('addresses.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


# 5-day weather forecast

import requests

def weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print(f"5-Day Weather Forecast for {city}:\n")

        for item in data["list"]:
            dt = item["dt_txt"]
            temp = item["main"]["temp"]
            feels_like = item["main"]["feels_like"]
            humidity = item["main"]["humidity"]
            description = item["weather"][0]["description"].capitalize()
            wind_speed = item["wind"]["speed"]
            wind_deg = item["wind"]["deg"]
            wind_gust = item["wind"].get("gust", "N/A")
            rain_volume = item.get("rain", {}).get("3h", 0)

            print(f"Date & Time: {dt}")
            print(f"Temperature: {temp}K (Feels like: {feels_like}K)")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description}")
            print(f"Wind: {wind_speed} m/s, Direction: {wind_deg}°, Gust: {wind_gust} m/s")
            print(f"Rain (last 3h): {rain_volume} mm")
            print("-" * 50)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather details: {e}")

city = input("Enter city: ")
weather(city, "70b7197efa3f029aa3229d47f25eed19")


# Create Database
import sqlite3

conn = sqlite3.connect("student.db")
conn.close()