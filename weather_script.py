import requests

def get_weather(place, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        city = data['name']
        print(f"Weather in {city}: {weather}, {temp}°C")
    else:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")

if __name__ == "__main__":
    place = input("Enter a city or place: ")
    api_key = "07d155d5f4af5efa48f5a5e319ac89a9"
    get_weather(place, api_key)
