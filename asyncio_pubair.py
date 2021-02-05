import asyncio
from aiohttp import ClientSession
from urllib.parse import unquote
from pprint import pprint

from pubair.msr_stn import Measurement_Station
from pubair.const import API_KEY


async def main():
    """Example function for testing Pub Air Library"""
    msrstn = Measurement_Station(API_KEY)
    params = [
        {
            "returnType": "json",
            "numOfRows": "10",
            "pageNo": "1",
            "addr": "서울",
            "stationName": "영등포구",
        },
        {
            "returnType": "json",
            "numOfRows": "10",
            "pageNo": "1",
            "umdName": "영등포구",
        },
        {
            "returnType": "json",
            "tmX": "191014.742452",
            "tmY": "447426.718548",
        },
    ]

    res = await msrstn.get_msr_stn_list(params[0])
    res2 = await msrstn.get_tm_stdr_crdnt(params[1])
    res3 = await msrstn.get_nearby_msr_stn_list(params[2])

    pprint(res)
    pprint(res2)
    pprint(res3)

    await msrstn.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())