
#Links the top youtube video result

import telegram
import os
import requests
from telegram.ext import MessageHandler, Filters, CommandHandler,Updater
from bs4 import BeautifulSoup

"""
The video method will return the first video in the youtube search result.
It will skip over any channels and links that are not explicitly videos.
Uses BeautifulSoup to receive the html code, with the rest of the code
extracting the link of the video we want to link.
"""

def video(receivedMessage, message2, context):
    message2 = message2.replace(' ', '+')
    url = 'https://www.youtube.com/results?search_query='
    response = requests.get(url + message2,timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    counter = 0 # Amount of lines we've gone through
    skipLines =  47 # The number of html lines to skip over in every youtube search
    keywords = ["google", "user", "channel"] # Words that we do NOT wantto link
    keywordInLine = False
    notLinked = True # Used to only link 1 video
    context.bot.send_message(chat_id=receivedMessage.chat_id, text='initial 1 test for eric')
    # Loop through all 'a' lines that have an 'href' link to search for top resulted video
    for link in content.find_all('a'):
        counter+=1
        context.bot.send_message(chat_id=receivedMessage.chat_id, text='test for eric')
        for i in keywords:
            if i in link.get('href'):
                keywordInLine = True
        if counter >= skipLines and keywordInLine ==  False and notLinked == True:
            context.bot.send_message(chat_id=receivedMessage.chat_id, text= 'youtube.com' + link.get('href'))
            notLinked = False
        keywordInLine = False    
        
