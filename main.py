import random
import telebot
import json


token = '6220738348:AAHWaN5V6DrCJWXVaVNJhdapaE82uYEMeWo'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Дворцы')
    item2 = telebot.types.KeyboardButton('Парки')
    item3 = telebot.types.KeyboardButton('Мосты')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать! О какой достопримечательности Санкт-Петербурга найти статью?', reply_markup=markup)

with open('Palace.json', 'r', encoding='utf-8') as pal:
    some_dict = json.load(pal)
    print(some_dict)



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower()=='дворцы':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Юсуповский дворец')
        item2 = telebot.types.KeyboardButton('Михайловский дворец')
        item3 = telebot.types.KeyboardButton('Екатерининский дворец')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Выбери дворец', reply_markup=markup)
        bot.register_next_step_handler(message, palace)
    elif message.text.lower()=='парки':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Екатерининский парк')
        item2 = telebot.types.KeyboardButton('Летний сад')
        item3 = telebot.types.KeyboardButton('Таврический сад')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Выбери парк', reply_markup=markup)
        bot.register_next_step_handler(message, palace)
    elif message.text.lower()=='мосты':
        bot.send_message(message.chat.id, 'В Санкт-Петербурге 800 мостов')
    else:
        bot.send_message(message.chat.id, 'Такой достопримечательности в списке нет')


@bot.message_handler(content_types=['text'])
def palace(message):
    bot.send_message(message.chat.id, some_dict[message.text])



bot.polling(none_stop=True)





