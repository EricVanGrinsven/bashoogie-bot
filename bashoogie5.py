import telegram
import os
import requests
from youtube import video
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
    if "@Jeffy" in message2 or "@BashoogieBot" in message2:
        message2 = message2.replace('@Jeffy', '')
        message2 = message2.replace('@BashoogieBot', '')
        video(receivedMessage, message2,context)
        #context.bot.send_message(chat_id=receivedMessage.chat_id, text=receivedMessage.message_id)
        
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