import telebot
from decouple import config
from datetime import datetime

API_KEY = config("TOKEN_TELEGRAM")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def responder(msg):
    # To send a Message File
    bot.reply_to(
        msg, msg.text+'___->'+msg.date)


# bot.polling()

bot.infinity_polling()
