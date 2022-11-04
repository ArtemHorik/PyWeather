import asyncio
import winsdk.windows.devices.geolocation as wdg
from typing import NamedTuple

import config


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


async def _get_coords() -> tuple:
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    latitude, longitude = pos.coordinate.latitude, pos.coordinate.longitude
    if config.USE_ROUNDED_COORDS:
        latitude, longitude = map(lambda x: round(x, 1), [latitude, longitude])
    return latitude, longitude


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    else:
        return Coordinates(*map(
            lambda x: round(x, 1),
            [coordinates.latitude, coordinates.longitude]))


def get_gps_coordinates() -> Coordinates:
    try:
        coords = asyncio.run(_get_coords())
        return _round_coordinates(Coordinates(*coords))
    except PermissionError:
        print("ERROR: You need to allow applications to access you location in Windows settings")
