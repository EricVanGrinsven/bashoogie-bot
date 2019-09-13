import telegram
import os
from telegram.ext import CommandHandler,  MessageHandler, Filters

bot = telegram.Bot(token='771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4')
#print(bot.get_me())
TOKEN = "771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
def talk(update, context):
    #context.bot.send_message(chat_id=update.message.chat_id, text="fuck u")
# add handlers
talk_handler = MessageHandler(Filters.text, talk)
dispatcher.add_handler(talk_handler)    
def main()
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://young-waters-97525.herokuapp.com/" + TOKEN)
    updater.idle()

if __name__ == "__main__":asdkjf sadf
    maidfn()sdflnsalkdfja