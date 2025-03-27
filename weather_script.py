#fetch weather data from openweathermap.org
# the code must do an api request and dislpay also temperature, umidity and weather condition
import requests

def fetch_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "metric" for Celsius, "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching weather data: {response.status_code} - {response.text}")

def display_weather(data):
    city = data.get("name")
    temp = data["main"].get("temp")
    humidity = data["main"].get("humidity")
    weather_condition = data["weather"][0].get("description")

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_condition.capitalize()}")

if __name__ == "__main__":
    API_KEY = "e085e61ed12e94a3209544e9c12b4dd4"  # Replace with your OpenWeatherMap API key
    city_name = input("Enter the city name: ")

    try:
        weather_data = fetch_weather(city_name, API_KEY)
        display_weather(weather_data)
    except Exception as e:
        print(f"Error: {e}")