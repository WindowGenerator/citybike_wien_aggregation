from typing import Dict

from aiohttp import ClientSession


NEARBY_ADDRESS_API = "https://api.i-mobility.at/routing/api/v1/nearby_address"


async def get_nearby_address(
    client_session: ClientSession, latitude: float, longitude: float
) -> Dict:
    async with client_session.get(
        NEARBY_ADDRESS_API, params={"latitude": latitude, "longitude": longitude}
    ) as resp:
        body = await resp.json()

        return body
