import telegram
import os
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler
TOKEN = "771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
#dispatcher = updater.dispatcher
#def echo(update, context):
 #   context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
# add handlers
#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)    
def echo(update, context):
    message2 = update.message.text
    user2 = update.message.from_user
    context.bot.send_message(chat_id=update.message.chat_id, text=message2)
    
    if "fuck" in  message2:
        context.bot.send_message(chat_id=update.message.chat_id, text=message2)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
bot = telegram.Bot(token='771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4')

def main():
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://young-waters-97525.herokuapp.com/" + TOKEN)
    updater.idle()

if name == "main":
    main()