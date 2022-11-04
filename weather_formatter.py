from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Formats PyWeather data in string"""
    return (f"{weather.city}, temperature {weather.temperature}°C, "
            f"{weather.weather_type.value}\n"
            f"Sunrise: {weather.sunrise.strftime('%H:%M')}\n"
            f"Sunset: {weather.sunset.strftime('%H:%M')}\n"
            )

