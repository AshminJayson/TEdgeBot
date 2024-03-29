import flask #Import flask package
import telebot #Import PyTeleBotAPI


TOKEN = "5788222546:AAEF4VgA6wQw1IBt3Vh66gODwJG-kcCHF7I"
URL = "https://1a09-103-183-83-106.in.ngrok.io/"

bot = telebot.TeleBot(TOKEN, threaded = False)


app = flask.Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index() :

    #Transfer POST request to URL as telebot update
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

#Set Webhook
def setWebhook() : 
    bot.remove_webhook()
    bot.set_webhook(url = URL)


#Handle commands
@bot.message_handler(commands = ['start', 'help'])
def startHandler(message) : 
    if message.text == "/start" : 
        bot.send_message(message.chat.id, "----")
    elif message.text == '/help' : 
        bot.send_message(message.chat.id, "++++")


#Handle generic text messages
@bot.message_handler(content_types=['text'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "You've sent me a text message")


if __name__ == '__main__':
    setWebhook()
    app.run(debug = True)