import requests
from requests.structures import CaseInsensitiveDict

url = "https://10.130.3.17:31013/sign"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/Json"
MyFile = open("text2.txt").read()
print(MyFile)
data = MyFile


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

