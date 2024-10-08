import telebot
from random import *
import json
import requests
films = []

API_URL='https://7012.deeppavlov.ai/model'

API_TOKEN = '7720214175:AAEll4eDK4yKwFeYL-qjH5ss7mm_cJJbKkY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start']) #decorator
def start_message(message):

    films.append("Matrix")
    films.append("Solyaris")
    films.append("Lord of the Rings")
    films.append("Interstellar")
    films.append("Inception")
    bot.send_message(message.chat.id, "Default Movies' list has been uploaded!")

@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id, "Here is the list of movies")
        bot.send_message(message.chat.id, ", ".join(films))
    except:
        bot.send_message(message.chat.id, "Movies' list is turned out to be empty!")

@bot.message_handler(commands=['save'])
def save_all(message):
    with open("films.json", "w", encoding='utf-8') as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    bot.send_message(message.chat.id, "Your movies' list has been successfully saved in file films.json")

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "I couldn't find anything for your request, sorry :(")

@bot.message_handler(content_types=['text'])
def get_text_message(message):
     if 'дела' in message.text.lower():
         bot.send_message(message.chat.id, "Дела отлично! Как сам?")

bot.polling()
