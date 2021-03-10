import telebot
# import uploader

from dotenv import load_dotenv
import os

import requests

load_dotenv()
token = os.getenv("TG_BOT_KEY")
bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

@bot.message_handler(content_types=['document'])
def handle_files(message):
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    name = message.document.file_path
    print(name)
    # url = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path)
    # file = requests.get(url)
    # # print(file)
    # print(file_info.file_path)
    # file1 = open("file_temp.png", "wb+")
    # file1.write(file.content)
    # file1.close()

bot.polling()