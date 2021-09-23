from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
app = Flask(__name__)
#TODO
print("SomeOneHelpMe2")
URL = 'https://api.telegram.o/'


def write_json(data, filename = "answer.json"):
    with open(filename, "w") as f:
        json.dump(data,f, indent=2,ensure_ascii=False)


def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    #write_json(r.json())
    return r.json()
def send_message(chat_id,text='bla-bla'):
    url=URL+ 'sendMessage'
    answer = {"chat_id":chat_id, 'text':text}
    r = requests.post(url,json=answer)
    return r.json()

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == "POST":
        r = request.get_json()
        write_json(r)
        return jsonify(r)

def main():
    # r = requests.get(URL+ "getMe")
   # write_json(r.json())
  #  print(r.json())
    #get_updates()
 #   r=get_updates()
  #  chat_id = r["result"][-1]["message"]["chat"]["id"]
   # print([chat_id])
   # send_message(chat_id)
   pass

if __name__ == '__main__':
   # main()
    app.run()
