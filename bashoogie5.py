"""
Main Driver of our telegram bot. Delegates which messages need responses
and where to get those responses from.  Our bot receives messages via
webhooks, and the server is hosted on heroku.
"""
import telegram
import os
import requests
import random
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
    message2 = message2.replace('/youtube ', '')
    video(receivedMessage, message2,context)
"""
Instructions on bot startup
"""
def start(update, context):
    receivedMessage = update.message
    speech = "Hello, I am Jeffy.\n\
    To send youtube video, type '/youtube' followed by your video\n\
    Type '/random + n' to receive a random number 'n' from 0-n\
    Type '/help' for these options again"
    context.bot.send_message(chat_id=receivedMessage.chat_id, text=speech)
"""
Instructions/help for user
"""
def help(update, context):
    receivedMessage = update.message
    speech = "To send youtube video, type '/youtube' followed by your video\n\
    Type '/random + n' to receive a random number 'n' from 0-n\
    Type '/help' for these options again"
    context.bot.send_message(chat_id=receivedMessage.chat_id, text= speech)
"""
Inside Joke with my friends
"""
def bebsi(update, context):
    receivedMessage = update.message
    speech = "DAAAAAAAAAAAAAAAAAAAAAAAASSSSSSSSSSSSSSSSS BEASHTTTTTTTTTTTTT"
    context.bot.send_message(chat_id=receivedMessage.chat_id, text= speech)
"""
Generates random number from 0-n, with n chosen by the user
"""    
def randomNum(update, context):
    receivedMessage = update.message
    receivedMessage.text = receivedMessage.text.replace('/random ', '')
    #If the user does not give an error, throw error to just a chat message
    try:
        number = int(receivedMessage.text)
        context.bot.send_message(chat_id=receivedMessage.chat_id, text= random.randint(0, number))
    except: 
        context.bot.send_message(chat_id=receivedMessage.chat_id, text= "Please type an integer with the command")
"""
Randomly selected greeting to send to the user
"""
def greeting(update, context):
    greetings = ["hello", "what's up, my dude?",  "yeet for treat"]
    randomGreeting = random.randint(0, len(greetings)-1)
    context.bot.send_message(chat_id=receivedMessage.chat_id, text= greetings[randomGreeting])
    
youtube_handler = CommandHandler('youtube', executeYoutube)
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
bebsi_handler = CommandHandler('bebsi', bebsi)
rand_handler = CommandHandler('random', randomNum)
greeting_handler = CommandHandler('hello', greeting)

dispatcher.add_handler(youtube_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(bebsi_handler)
dispatcher.add_handler(rand_handler)
dispatcher.add_handler(greeting_handler)
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