import asyncio

from typing import Dict, List

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientResponseError
from aiohttp.web import HTTPTooManyRequests
from src.apis.nearby_address import get_nearby_address


async def agregate(client_session: ClientSession, stations: List[Dict]) -> List[Dict]:
    converted_stations = []

    for station in stations:
        converted_station = {
            "id": station["id"],
            "name": station["name"],
            "description": station["description"],
            "boxes": station["boxes"],
            "free_boxes": station["free_boxes"],
            "free_bikes": station["free_bikes"],
        }

        attempts = 5

        while True:
            try:
                nearby_address = await get_nearby_address(
                    client_session, station["latitude"], station["longitude"]
                )
                converted_station["address"] = nearby_address["data"]["name"]
                break
            except ClientResponseError as exc:
                if exc.status != HTTPTooManyRequests.status_code:
                    raise
                if attempts <= 0:
                    raise
                attempts -= 1

                await asyncio.sleep(2)

        converted_station["active"] = station["status"] == "aktiv"
        converted_station["coordinates"] = [station["longitude"], station["latitude"]]
        converted_station["free_ratio"] = station["free_boxes"] / station["boxes"]

        converted_stations.append(converted_station)

        await asyncio.sleep(0.1)

    converted_stations.sort(
        key=lambda converted_station: (
            -converted_station["free_bikes"],
            converted_station["name"],
        )
    )

    return converted_stations
