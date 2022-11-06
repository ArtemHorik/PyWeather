USE_ROUNDED_COORDS = False
SAVE_TO_TXT = True
SAVE_TO_JSON = False
OPENWEATHER_API = "ENTER YOR API HERE"
OPENWEATHER_URL = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}&appid="
        + OPENWEATHER_API + "&units=metric"
)
