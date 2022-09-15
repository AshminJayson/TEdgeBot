from flask import Flask #For defining Web Application
from flask import request #For recieving ChatBot POST and GET Requests
from flask import Response #To return Response to Bot
import requests #For messaging passing through Telegram Bot API

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        print(msg)

        return Response('ok', status = 200)
    else:
        return "<h2>plain text</h2>"

if __name__ == '__main__':
    app.run()