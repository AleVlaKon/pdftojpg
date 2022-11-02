import telebot

bot = telebot.TeleBot("5765652382:AAGXzpbo-f_LPuVUR4985TfzhMSZMSIH9_A", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.send_message(message.chat.id, message.text)

bot.infinity_polling()