

#Function of Parsing JSON POST request
def parseMessage(message) :
    # print("Message -> ", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("Chat ID -> ", chat_id, "\nText -> ", txt)
    return chat_id, txt

#Function to invoke telegram API to send messages
def telSendMessage(chat_id, text) :
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        'chat_id' : chat_id,
        'text' : text
    }

    r = requests.post(url, json = payload)
    return r

#Function to invoke telegram API to send images
def telSendImage(chat_id, img_url, caption) :
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    payload = {
        'chat_id' : chat_id,
        'photo' : img_url,
        'caption' : caption
    }

    r = requests.post(url, json = payload)
    return r

#The functions to implement the other post request can be done throught similar calls 
#to the Telegram Bot API

#Index page route and __main__ function
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, txt = parseMessage(msg)

        # if txt == "Hey!" :
        #     # print("condition evaluated")
        #     telSendMessage(chat_id, "Hello there....")
        # else : 
        #     telSendMessage(chat_id, "I'm not trained for such conversations")

        return Response('ok', status = 200)
    else:
        return "<h2>plain text</h2>"