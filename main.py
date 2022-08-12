import telebot
from decouple import config
from datetime import datetime,timezone
import time
import pytz

API_KEY = config("TOKEN_TELEGRAM")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def responder(msg):
    # To send a Message File
    timezone_local = datetime.now(timezone.utc).astimezone().tzinfo
    info = f'''
    Unix Timestemp: {msg.date}
    Time: {datetime.fromtimestamp(msg.date,timezone_local)}
    Timezone: {time.tzname}
    '''
    bot.reply_to(
        msg, info)


# bot.polling()

bot.infinity_polling()
