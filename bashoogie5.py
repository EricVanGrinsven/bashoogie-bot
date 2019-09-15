import telegram
import os
import requests
from telegram.ext import MessageHandler, Filters, CommandHandler,Updater
from bs4 import BeautifulSoup
TOKEN = "771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
#def echo(update, context):
 #   context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
# add handlers
#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)    
def echo(update, context):
    receivedMessage =update.message
    message2 = receivedMessage.text
    user2 = receivedMessage.from_user
    #context.bot.send_message(chat_id=receivedMessage.chat_id, text=receivedMessage.message_id)
    message2 = message2.replace(' ', '+')
    url = 'https://www.youtube.com/results?search_query='
    response = requests.get(url + message2,timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    counter = 0
    set = true
    for link in content.find_all('a'):
        counter+=1
        if counter == 47 && "google" not in link.get('href') && set == true
            context.bot.send_message(chat_id=receivedMessage.chat_id, text= 'youtube.com' + link.get('href'))
            set = false
    #if "fuck" in message2:
    #    context.bot.send_message(chat_id=update.message.chat_id, text=message2)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
bot = telegram.Bot(token='771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4')

def main():
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://young-waters-97525.herokuapp.com/" + TOKEN)
    updater.idle()

if __name__ == "__main__":
    main()