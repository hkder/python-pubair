import asyncio
from aiohttp import ClientSession
from urllib.parse import unquote

from pubair.msr_stn import Measurement_Station
from pubair.const import API_KEY


async def main():
    """Example function for testing Pub Air Library"""

    async with Measurement_Station(API_KEY) as msrstn:
        query_params = {
            "returnType": "json",
            "numOfRows": "10",
            "pageNo": "1",
            "addr": "서울",
            "stationName": "종로구",
        }
        res = await msrstn.get_msr_stn_list(query_params)
        print(res)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())