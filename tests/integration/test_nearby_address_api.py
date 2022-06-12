from typing import Dict, Tuple

import pytest

from aiohttp import ClientSession
from src.apis.nearby_address import get_nearby_address


@pytest.mark.parametrize(
    "coordinates, expected_name",
    [
        ((16.375869, 48.190693), "???"),
        ((48.185165595330574, 16.3740655721665), "Südtiroler Platz 12, 1100 Wien"),
    ],
)
@pytest.mark.asyncio
async def test_nearby_address_simple(
    coordinates: Tuple[float, float], expected_name: str, client_session: ClientSession
) -> None:
    nearby_address = await get_nearby_address(
        client_session, coordinates[0], coordinates[1]
    )

    assert isinstance(nearby_address, Dict)
    assert nearby_address["data"]["name"] == expected_name
