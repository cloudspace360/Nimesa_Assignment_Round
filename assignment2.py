# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HytwfEdVVNy3Mzt1spnxX9pP3joYhNfB

#Assignment 2:

The assignment is based on an API, wherein you will have to use the data provided in the API and write a program to get the Weather report, wind speed and pressure from the user and get the result based on the API.


Nimesa Technology
"""

import requests

def get_weather_data():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Exiting.")
        exit()

def get_temperature(data, target_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_time:
            return entry['main']['temp']
    return None

def get_wind_speed(data, target_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_time:
            return entry['wind']['speed']
    return None

def get_pressure(data, target_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_time:
            return entry['main']['pressure']
    return None

def main():
    weather_data = get_weather_data()

    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            target_time = input("Enter date with time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(weather_data, target_time)
            if temperature is not None:
                print(f"Temperature at {target_time}: {temperature}°C")
            else:
                print("Data not found for the given date and time.")

        elif choice == '2':
            target_time = input("Enter date with time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(weather_data, target_time)
            if wind_speed is not None:
                print(f"Wind Speed at {target_time}: {wind_speed} m/s")
            else:
                print("Data not found for the given date and time.")

        elif choice == '3':
            target_time = input("Enter date with time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(weather_data, target_time)
            if pressure is not None:
                print(f"Pressure at {target_time}: {pressure} hPa")
            else:
                print("Data not found for the given date and time.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()