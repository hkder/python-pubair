# 한국환경공단_에어코리아_측정소정보 API Asyncio 라이브러리
# https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073877
import asyncio
import aiohttp
import async_timeout
from urllib.parse import unquote
from typing import Any, Optional
from .exceptions import PubAirError, APIConnectionError


class Measurement_Station:
    def __init__(
        self,
        auth_key: str = None,
        base_url: str = "http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc",
        request_timeout: int = 10,
        session: aiohttp.ClientSession = None,
    ):
        """Initialize the Measure Station API Class"""
        self._auth_key = unquote(auth_key)
        self._base_url = base_url
        self._request_timeout = request_timeout
        self._session = session

    async def _request(
        self,
        method: str,
        url: str,
        params: Optional[dict] = None,
    ) -> Any:
        if self._session is None:
            self._session = aiohttp.ClientSession()

        try:
            with async_timeout.timeout(self._request_timeout):
                response = await self._session.request(method, url, params=params)
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            raise APIConnectionError(
                "Timeout occurred while connecting to Open API Server"
            ) from exception
        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            socket.gaierror,
        ) as exception:
            raise APIConnectionError(
                "Error occurred while connecting to Open API Server"
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            text = await response.text()
            raise PubAirError(
                "Unexpected response from the Open API Server",
                {"Content-Type": content_type, "response": text},
            )
        return await response.json()

    async def get_msr_stn_list(self, params):
        """
        [Parameter List]
        serviceKey: 서비스키
        returnType: xml 혹은 json
        numOfRows: 한 페이지 결과 수
        pageNo: 페이지 번호
        addr: 주소
        stationName: 측정소명
        """
        end_url = self._base_url + "/getMsrstnList"
        query_params = {
            "serviceKey": self._auth_key,
            "returnType": params["returnType"],
            "numOfRows": params["numOfRows"],
            "pageNo": params["pageNo"],
            "addr": params["addr"],
            "stationName": params["stationName"],
        }
        response = await self._request(method="get", url=end_url, params=query_params)
        return response

    async def get_nearby_msr_stn_list(self):
        pass

    async def get_tm_stdr_crdnt(self):
        pass

    async def close(self) -> None:
        """Close open client session."""
        if self._session:
            await self._session.close()

    async def __aenter__(self) -> "Measurement_Station":
        """Asnyc enter."""
        return self

    async def __aexit__(self, *exec_info) -> None:
        """Async exit."""
        await self.close()
