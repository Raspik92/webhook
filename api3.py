import requests
from requests.structures import CaseInsensitiveDict

url = "https://10.130.3.17:31013/sign"

headers = CaseInsensitiveDict()
headers["Content-type"] = "application/json"

data = {"version": 2, "client": "SnI", "passcode": "L2oZIzj0DAQcEJzAlAgEBBCA522KpDarp",  "healthdata": { "ver": "1.3.0", "nam": { "fn": "À¯ÍÃÎÍÅ Ì²ÍÒÑÀ", "fnt": "AYINGONE MINTSA", "gn": "Ê²Ë²ª ÄÆÈÐ²", "gnt": "KYLIE  JIRI" }, "dob": "1992-10-31", "v": [ { "tg": "840539006", "vp": "1119349007", "mp": "EU/1/20/1507", "ma": "ORG-100031184", "dn": 2, "sd": 2, "dt": "2021-08-20", "co": "UA", "is": "State Enterprise \"DIIA\"", "ci": "URN:UVCI:01:UA:1798F47A8F9847598CA2286D933FFB25"}]}, "issuedat": 1638554164, "expiration": 1660942800}


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
