import json
from typing import Protocol, TypedDict
from pathlib import Path
from datetime import datetime

from weather_formatter import format_weather
from weather_api_service import Weather


class WeatherStorage(Protocol):
    """Interface for any storage saving weather data"""

    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class TextFileWeatherStorage:
    """Saves weather to a text file"""

    def __init__(self, file: Path):
        self.file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self.file, 'a') as f:
            f.write(f"{now.strftime('%d-%m-%Y %H:%M:%S')}\n{formatted_weather}\n")


class HistoryRecord(TypedDict):
    date: str
    weather: str


class JSONFileWeatherStorage:
    """Saves weather to a json file"""

    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append({
            "date": str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')),
            "weather": format_weather(weather)
        })
        self._write(history)

    def _init_storage(self) -> None:
        if not self._jsonfile.exists():
            self._jsonfile.write_text("[]")

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._jsonfile, 'r') as f:
            return json.load(f)

    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._jsonfile, 'w') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Save weather data to storage"""
    storage.save(weather)

