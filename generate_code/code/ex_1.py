openweather_key = "fde0547578e2fbcd9263abba8d35e539"


def fetch_weather_from_openweather(city_name):
    """
    Fetches and returns current weather data for the specified city using the OpenWeatherMap API.

    The function sends a GET request to the OpenWeatherMap API and returns the weather data in JSON format.
    The data includes temperature, humidity, pressure, weather description, and more, based on the city's name provided.

    Parameters:
        city_name (str): The name of the city for which to fetch the weather data.
                         It should be in the format recognized by the OpenWeatherMap API,
                         usually "City name,Country code" (e.g., "London,UK").

    Returns:
        dict: A dictionary containing the weather data returned from the OpenWeatherMap API.
              The structure of the dictionary depends on the JSON response from the API.
              Typical keys include 'main' for temperature and pressure information,
              'weather' for the description of the current weather, 'wind' for wind data, etc.

    Raises:
        requests.exceptions.HTTPError: An error occurs from the HTTP request to the OpenWeatherMap API.
        ValueError: The provided city name is not valid or recognized by the API.

    Usage Example:
        >>> api_key = "your_api_key_here"
        >>> city_name = "New York,US"
        >>> weather_data = fetch_weather_openweathermap(city_name, api_key)
        >>> print(weather_data)

    Note:
        Ensure that you have an active internet connection and that your API key is valid and has not exceeded its request limits.
        Also, check the city name format and ensure it matches the format expected by the OpenWeatherMap API.
    """