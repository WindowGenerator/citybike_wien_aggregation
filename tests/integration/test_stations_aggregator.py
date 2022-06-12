from typing import List

import pytest

from aiohttp import ClientSession
from src.aggregators.stations import agregate
from src.apis.stations import get_stations


@pytest.mark.asyncio
async def test_stations_aggregator_simple(client_session: ClientSession) -> None:
    aggregated_stations = await agregate(
        client_session, await get_stations(client_session)
    )

    assert isinstance(aggregated_stations, List)

    for station in aggregated_stations:
        assert "active" in station and isinstance(station["active"], bool)
        assert "address" in station and isinstance(station["address"], str)
        assert "coordinates" in station and isinstance(station["coordinates"], List)
        assert "free_ratio" in station and isinstance(station["free_ratio"], float)
