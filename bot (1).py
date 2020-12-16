import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot('1462014820:AAEW_fDvBHVoTF-YCl_NU_XdAxpEGJeHULs')
@bot.message_handler(commands=['start'])
def welcome(message):
    photo = open('sex/aues.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Добро пожаловать,{0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы решать ваши студенческие проблемы.".format(message.from_user, bot.get_me()), parse_mode='html',  reply_markup=markup)


       # keyboard
    
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Полезная информация для студентов")
markup.add(item1)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Полезная информация для студентов':
        bot.send_message(message.chat.id, 'Сейчас помогу')          
        markup = types.InlineKeyboardMarkup()
        item1 = btn_my_site = types.InlineKeyboardButton(text='восстонавление пароля', url='http://recovery.aues.kz/new-sbros.php')
        markup.add(btn_my_site)
        item2 = btn_my_site = types.InlineKeyboardButton(text='информация для абитуриентов', url='https://aues.edu.kz/ru/site/admissions')
        markup.add(btn_my_site)
        item3 = btn_my_site = types.InlineKeyboardButton(text='получение онлайн справки для студентов', url='https://aues.edu.kz/ru/cos')
        markup.add(btn_my_site)
        item4 = btn_my_site = types.InlineKeyboardButton(text='онлайн библиотека АУЭС', url='https://aues.edu.kz/ru/site/library')
        markup.add(btn_my_site)
        item5 = btn_my_site = types.InlineKeyboardButton(text='расписание', url='https://aues.arhit.kz/rasp/')
        markup.add(btn_my_site)
        item6 = btn_my_site = types.InlineKeyboardButton(text='вакантные образовательные гранты', url='https://aues.edu.kz/ru/students/konkurs')
        markup.add(btn_my_site)
                
    bot.send_message(message.chat.id, "Полезная информация для студентов", reply_markup = markup)
 
# RUN
bot.polling(none_stop=True)
