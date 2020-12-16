import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать,{0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть вашей слугой.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    # keyboard
    
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("")


markup.add(item1)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '':
            bot.send_message(message.chat.id, '')            
            markup = types.InlineKeyboardMarkup()
            item1 = btn_my_site = types.InlineKeyboardButton(text='', url='')
            markup.add(btn_my_site)
            item2 = btn_my_site = types.InlineKeyboardButton(text='', url='')
            markup.add(btn_my_site)
            item3 = btn_my_site = types.InlineKeyboardButton(text='', url='')
            markup.add(btn_my_site)

        elif message.text == ''
            bot.send_message(message.chat.id, '')
            
        else:
            bot.send_message(message.chat.id,'')         
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
