from flask import Flask #For defining Web Application
from flask import request #For recieving ChatBot POST and GET Requests
from flask import Response #To return Response to Bot
from flask import abort
import telebot
import requests #For messaging passing through Telegram Bot API

TOKEN = "5788222546:AAEF4VgA6wQw1IBt3Vh66gODwJG-kcCHF7I"
URL = "https://b409-103-183-83-106.in.ngrok.io/"

bot = telebot.TeleBot(TOKEN, threaded = False)


app = Flask(__name__)



#Set up webhook
@app.route('/', methods = ['GET', 'POST'])
def index() :
    # bot.remove_webhook()
    bot.set_webhook(url = URL)

    #Setting update state so that message handler is called
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)
    

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_start_help(msg):
    bot.send_message(2037921516, "Reshma Saju is super dumb and mean")
    # bot.reply_to(msg, "Hey there ~ ")


if __name__ == '__main__':
    app.run(debug = True)