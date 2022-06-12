import pytest_asyncio

from aiohttp import ClientSession


@pytest_asyncio.fixture
async def client_session() -> ClientSession:
    async with ClientSession(raise_for_status=True) as client:
        yield client
