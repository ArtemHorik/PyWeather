from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exception import ApiServiceError


def main():
    coordinates = get_gps_coordinates()
    try:
        weather = get_weather(coordinates)
        print(format_weather(weather))
    except ApiServiceError:
        print("Can't get weather from Weather-API service")
        exit(1)
    input('Press enter to exit...')


if __name__ == '__main__':
    main()
