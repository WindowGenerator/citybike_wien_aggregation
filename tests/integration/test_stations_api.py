from typing import List

import pytest

from aiohttp import ClientSession
from src.apis.stations import get_stations


@pytest.mark.asyncio
async def test_stations_simple(client_session: ClientSession) -> None:
    stations = await get_stations(client_session)

    assert isinstance(stations, List)
