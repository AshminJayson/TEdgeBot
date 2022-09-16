from flask import Flask #For defining Web Application
from flask import request #For recieving ChatBot POST and GET Requests
from flask import Response #To return Response to Bot
import telebot
import requests #For messaging passing through Telegram Bot API

TOKEN = "5788222546:AAEF4VgA6wQw1IBt3Vh66gODwJG-kcCHF7I"
URL = "https://13cd-103-160-194-195.in.ngrok.io/"

bot = telebot.TeleBot(TOKEN)


app = Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(662495469, "This is a text message which isn't getting sent how I want it to.")
    bot.reply_to(message, "Hey there ~ ")

@bot.message_handler(func = lambda msg : len(msg) > 2 )
def parseMessage(msg):
    print(msg)

@app.route('/', methods = ['GET', 'POST'])
def setWebHook():
    #TelegramBot API is used to set up a webhook to the tunneling IP of ngrok
    bot.set_webhook(url = URL)

    if request.method == 'POST':
        msg = request.get_json()
        print(msg)

    return Response('ok', status = 200)


if __name__ == '__main__':
    app.run(debug = True)