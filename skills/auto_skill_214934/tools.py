def main():
    # Importing necessary libraries
    import requests
    
    # Function to get current weather
    def get_current_weather(location):
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        complete_url = f"{base_url}?q={location}&appid={api_key}"
        response = requests.get(complete_url)
        return response.json()
    
    # Function to get weather forecast
    def get_weather_forecast(location):
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        base_url = "http://api.openweathermap.org/data/2.5/forecast"
        complete_url = f"{base_url}?q={location}&appid={api_key}"
        response = requests.get(complete_url)
        return response.json()
    
    # Example usage
    location = input("Enter the location for weather information: ")
    current_weather = get_current_weather(location)
    forecast = get_weather_forecast(location)
    
    # Print current weather
    print("Current Weather:")
    print(current_weather['weather'][0]['description'])
    
    # Print forecast
    print("Forecast:")
    for forecast_day in forecast['list'][0:5]:  # Get the first 5 days forecast
        print(f"Day: {forecast_day['dt_txt']}")
        print(f"Weather: {forecast_day['weather'][0]['description']}")
        print(f"Temperature: {forecast_day['main']['temp']} K")
        print("------------")

if __name__ == "__main__":
    main()