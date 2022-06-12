import asyncio
import json
import logging

import aiohttp

from src.aggregators.stations import agregate
from src.apis.stations import get_stations


LOGGING_LEVEL = "DEBUG"

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)


async def main():
    async with aiohttp.ClientSession(raise_for_status=True) as client_session:
        aggregated_stations = await agregate(
            client_session, await get_stations(client_session)
        )

    with open("./out_data/stations.json", "wt") as fd:
        json.dump(aggregated_stations, fd)


if __name__ == "__main__":
    asyncio.run(main())
