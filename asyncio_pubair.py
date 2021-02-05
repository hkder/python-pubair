import asyncio
from aiohttp import ClientSession
from pprint import pprint

from pubair.pubair import PubAir
from pubair.const import API_KEY


async def main():
    async with ClientSession() as session:
        pubair = PubAir(API_KEY, "가람동", session)
        await pubair.fetching_data()
        station = pubair.get_station_information()
        data = pubair.get_current_airpollution()
        pprint(station)
        pprint(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())