import telebot

bot = telebot.TeleBot('1752289304:AAFvNjWCNotz18A0rU9TQlHug323MKzWYK0')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока', 'A')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
                    #сообщение отправляется отправляющему
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

#https://mastergroosha.github.io/telegram-tutorial/
#https://habr.com/ru/users/dimagorovtsov/posts/
#https://python-telegram-bot.readthedocs.io/en/stable/telegram.html
#https://habr.com/ru/post/442800/
bot.polling()
