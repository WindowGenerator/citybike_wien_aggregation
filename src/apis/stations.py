from typing import Dict, List

from aiohttp import ClientSession


STATIONS_API = "https://wegfinder.at/api/v1/stations"


async def get_stations(client_session: ClientSession) -> List[Dict]:
    async with client_session.get(STATIONS_API) as resp:
        body = await resp.json()

        return body
