str ='ci": fn": "VDASDvdsASDA", "fnt": "KUMAR", "gn": "VDvadsASDA","URN:UVCI:01:UA:800A72ED55FF4759A9052B779F6F5173"}]}, "issuedat": 1638017704, "expiration": 1669500000}'
import re

surname = input("\n ВВедите Фамилию: ")
name = input("Введите имя: ")
print(surname+" " + name)




# Заменить дату генерации
str3 = re.search("issuedat\"[:]\s\d{10}",str)

print(str3[0])
# Берем из запроса код
str4 = re.search("URN[:]UVCI[:]01[:]UA[:]\w{10,35}",str)
str5 = re.search("fn\"[:]\s{1,15}\"", str)
name = re.search("fn\"[:]\s\"[a-zA-Z]*", str)
surname = re.search("gn\"[:]\s\"[a-zA-Z]*", str)
print(name)
print(surname)
#print(str5)
print(str4[0])