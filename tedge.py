from flask import Flask #For defining Web Application
from flask import request #For recieving ChatBot POST and GET Requests
from flask import Response #To return Response to Bot
import telebot
import requests #For messaging passing through Telegram Bot API

TOKEN = "5788222546:AAEF4VgA6wQw1IBt3Vh66gODwJG-kcCHF7I"
bot = telebot.TeleBot(TOKEN)


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def setWebHook():
    #TelegramBot API is used to set up a webhook to the tunneling IP of ngrok
    bot.set_webhook(url = "https://0246-103-160-194-195.in.ngrok.io")

    if request.method == 'POST':
        msg = request.get_json()
        print(msg)

    return Response('ok', status = 200)



@bot.message_handler(commands = ['start', 'end'])
def send_welcome(msg) : 
    bot.reply_to(msg, "Hey there ~ ")


if __name__ == '__main__':
    app.run(debug = True)