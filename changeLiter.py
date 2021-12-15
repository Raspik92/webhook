import uuid
import datetime
import time
import unicodedata
timestamp = int(time.time())
dt = datetime.datetime.now()
myuuid = (str(uuid.uuid4())).upper().replace('-','')
#newstr = myuuid.replace('-','')
print(myuuid)
#(timestamp)
string = ''
resultTime = timestamp+180
print(resultTime)


#u = unicodedata(line.strip(), "utf-8")



