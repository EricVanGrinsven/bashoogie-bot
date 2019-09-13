import telegram
import os

bot = telegram.Bot(token='771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4')
#print(bot.get_me())
TOKEN = "771496641:AAFxDXFGa67rTkzJcnYo0BjDlwI77lpSXE4"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://young-waters-97525.herokuapp.com/" + TOKEN)

#updater.idle()
