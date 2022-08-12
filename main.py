import telebot
from decouple import config
from datetime import datetime
import time

API_KEY = config("TOKEN_TELEGRAM")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def responder(msg):
    # To send a Message File
    info = f'''
    Unix Timestemp: {msg.date}
    Time: {datetime.fromtimestamp(msg.date,tz=time.tzname[0])}
    Timezone: {time.tzname}
    '''
    bot.reply_to(
        msg, info)


# bot.polling()

bot.infinity_polling()
