import access
import os
import telebot
print("Starting bot")
bot = telebot.TeleBot(access.api_key)

@bot.message_handler(commands=['Greet'])
def Greet(message):
    bot.reply_to(message, "HEY pdr")

@bot.message_handler(commands=['Hey'])
def Hey(message):
    bot.send_message(message.chat.id, "HEY ")
    bot.send_message(message.chat.id, "HEY2 ")

bot.polling()
