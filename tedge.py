from flask import Flask #For defining Web Application
from flask import request #For recieving ChatBot POST and GET Requests
from flask import Response #To return Response to Bot
import requests #For messaging passing through Telegram Bot API

TOKEN = "5788222546:AAGlwyvaTp4IDfkRE7_6eZ554UirVaoET4w"

def parseMessage(message) :
    # print("Message -> ", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("Chat ID -> ", chat_id, "\nText -> ", txt)


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        parseMessage(msg)
        # print(msg)

        return Response('ok', status = 200)
    else:
        return "<h2>plain text</h2>"

if __name__ == '__main__':
    app.run()