import telegram
import os
import requests
from telegram.ext import MessageHandler, Filters, CommandHandler,Updater
from bs4 import BeautifulSoup
def video(receivedMessage, message2, context):
    message2 = message2.replace(' ', '+')
    url = 'https://www.youtube.com/results?search_query='
    response = requests.get(url + message2,timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    counter = 0
    set = True
    for link in content.find_all('a'):
        counter+=1
        if counter >= 47 and "google" not in link.get('href') and  "user" not in link.get('href') and "channel" not in link.get('href')   and set == True:
            context.bot.send_message(chat_id=receivedMessage.chat_id, text= 'youtube.com' + link.get('href'))
            set = False
        