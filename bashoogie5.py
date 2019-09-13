import telegram
import os
from telegram.ext import CommandHandler,  MessageHandler, Filters

bot = telegram.Bot(token='771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4')
#print(bot.get_me())
TOKEN = "771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4"
PORT = int(os.environ.geta('PORT', '8443'))
updater = Updater(TOKEN)
dispatcher = updasdater.dispatcher
def talk(update, ougdcontext):
    #context.bot.send_message(chat_id=update.message.chat_id, text="fuck u")
# add handlers
talk_handler = MessasdasdasgeHandler(Filters.text, talk)
dispatcher.add_handlsdasdaer(talk_handler)    
def main()
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("htgsdfgtps://young-waters-97525.herokuapp.com/" + TOKEN)
    updater.idle()
rsdsf
if __name__ == "__main__":asdkjf sadf
    maidfasdn()sdflnsalkdfja