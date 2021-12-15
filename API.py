import requests
from requests.structures import CaseInsensitiveDict

url = "https://dc.ukc.gov.ua/api/1/json/public/3200/00144acb84214a43b001bc5e16948b5bde448bc7"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/Json"

data = "{\"test\":\"test\"}"


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

