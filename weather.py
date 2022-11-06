from pathlib import Path

import config
from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exception import ApiServiceError
from history import save_weather, JSONFileWeatherStorage, TextFileWeatherStorage


def main():
    coordinates = get_gps_coordinates()
    try:
        weather = get_weather(coordinates)
        print(format_weather(weather))
        if config.SAVE_TO_TXT:
            save_weather(weather, TextFileWeatherStorage(Path.cwd() / "history.txt"))
        if config.SAVE_TO_JSON:
            save_weather(weather, JSONFileWeatherStorage(Path.cwd() / "history.json"))
    except ApiServiceError:
        print("Can't get weather from Weather-API service")
        exit(1)
    finally:
        input('Press enter to exit...')


if __name__ == '__main__':
    main()
