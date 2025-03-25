import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to get weather data")

if __name__ == "__main__":
    main()