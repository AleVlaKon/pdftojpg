import telebot
from telebot import types

bot = telebot.TeleBot("5765652382:AAGXzpbo-f_LPuVUR4985TfzhMSZMSIH9_A", parse_mode=None)

# markup = types.ReplyKeyboardMarkup()
# bt_pt34 = types.KeyboardButton("ПТ34")
# bt_pt23 = types.KeyboardButton("пт23")
# bt_pt12 = types.KeyboardButton("пт12")
# bt_ms30 = types.KeyboardButton("мс30")
# bt_rvyb = types.KeyboardButton("рвыб")
# bt_odmel = types.KeyboardButton("одмел")
# markup.row(bt_pt34, bt_pt23, bt_pt12)
# markup.row(bt_ms30, bt_rvyb, bt_odmel)
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.send_message(message.chat.id, message.text, reply_markup=markup)


@bot.message_handler(commands=["start"])
def start (message):
    #Клавиатура с кнопкой запроса локации
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="ПТ23", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Поделись местоположением", reply_markup=keyboard)

 #Получаю локацию
@bot.message_handler(content_types=['location'])
def location (message):
    if message.location is not None:
        print(message.location)
        print(message)

bot.polling(none_stop = True)
input()







bot.infinity_polling()