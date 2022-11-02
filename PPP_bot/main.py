import telebot

bot = telebot.TeleBot('5765652382:AAGXzpbo-f_LPuVUR4985TfzhMSZMSIH9_A')

@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode='html')



bot.polling(none_stop=True)

