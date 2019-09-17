"""
Main Driver of our telegram bot. Delegates which messages need responses
and where to get those responses from.  Our bot receives messages via
webhooks, and the server is hosted on heroku.
"""
import telegram
import os
import requests
from youtube import video
from telegram.ext import MessageHandler, Filters, CommandHandler, Updater
from bs4 import BeautifulSoup

TOKEN = os.getenv("TOKEN")
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

"""
echo will simply find which command was sent to the bot, and lead it to
the correct method using a switch statement. EX) /youtube will follow 
the youtube method and send the corresponding message
"""
def executeYoutube(update, context):
    receivedMessage =update.message
    message2 = receivedMessage.text
    user2 = receivedMessage.from_user
    """if "@Jeffy " not in message2 or "@BashoogieBot " not in message2:
        message2 = message2.replace('@Jeffy', '')
        message2 = message2.replace('@BashoogieBot', '')
        message2 = message2.replace('@Jeffy ', '')
        message2 = message2.replace('@BashoogieBot ', '')"""
    message2 = message2.replace('/youtube ', '')
    video(receivedMessage, message2,context)
youtube_handler = CommandHandler('youtube', executeYoutube)
#echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(youtube_handler)
bot = telegram.Bot(token=TOKEN)

"""
Set up the webhook to work with herokuapp
"""
def main():
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://young-waters-97525.herokuapp.com/" + TOKEN)
    updater.idle()

if __name__ == "__main__":
    main()