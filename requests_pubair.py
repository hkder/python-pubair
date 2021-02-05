import requests
from urllib.parse import unquote

url_endpoint = "http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList"
key = "u63qRRyqZfR34GrJCQRpqk777kJbnv1slAR5CrjElo6OZ%2FRsJwouWroU2xKGIgGqZUqTkiQWcA4Ox%2BgLO0qltg%3D%3D"
payload = {
    "serviceKey": unquote(key),
    "returnType": "json",
    "numOfRows": "10",
    "pageNo": "1",
    "addr": "서울",
    "stationName": "종로구",
}
res = requests.get(url_endpoint, params=payload)
print(res.status_code)
print(res.text)