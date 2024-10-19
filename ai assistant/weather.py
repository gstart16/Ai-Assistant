import requests

# Define your API key and base URL
API_KEY = "aec567d245374653aa94027f990e8b10"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch the weather data for a given city."""
    # Construct the complete API URL
    api_address = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # Use 'imperial' for Fahrenheit

    # Fetch data from the API
    response = requests.get(api_address)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data:", response.status_code)
        return None

def display_weather(data):
    """Display the weather information."""
    if data:
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("No weather data available.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    
    # Get weather data
    weather_data = get_weather(city_name)
    
    # Display the weather report
    display_weather(weather_data)