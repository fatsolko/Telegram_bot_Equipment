import telebot
import config

bot = telebot.TeleBot(config.token)

keyboard_start = telebot.types.ReplyKeyboardMarkup(True)
keyboard_start.row('Добавить', 'Удалить', 'Найти')
keyboard_adddel = telebot.types.ReplyKeyboardMarkup(True)
keyboard_adddel.row('R', 'C', 'VD', 'VT', 'DC/DC')
keyboard_size_res = telebot.types.ReplyKeyboardMarkup(True)
keyboard_size_res.row('0402', '0603', '0805', '1206', '1210', '2010', '2512')
keyboard_size_cap = telebot.types.ReplyKeyboardMarkup(True)
keyboard_size_cap.row('0402', '0603', '0805').row('1206', '1210', '2010', '2512').add('Эл-лит', 'Керамика', 'Плёнка')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, выбери действие /start', reply_markup=keyboard_start)
    bot.register_next_step_handler(message, send_question_element)


def send_question_element(message):
    if message.text.lower() == 'добавить':
        bot.send_message(message.chat.id, 'Какой элем?', reply_markup=keyboard_adddel)
        bot.register_next_step_handler(message, send_question_size_add)

    elif message.text.lower() == 'удалить':
        bot.send_message(message.chat.id, 'Какой', reply_markup=keyboard_adddel)
        bot.register_next_step_handler(message, send_question_size_add)

    elif message.text.lower() == 'найти':
        bot.send_message(message.chat.id, 'элемент', reply_markup=keyboard_adddel)
        bot.register_next_step_handler(message, send_question_size_add)


def send_question_size_add(message):
    if message.text.lower() == 'r':
        bot.send_message(message.chat.id, 'Типоразмер?', reply_markup=keyboard_size_res)
    elif message.text.lower() == 'c':
        bot.send_message(message.chat.id, 'Типоразмер или вид', reply_markup=keyboard_size_cap)
    elif message.text.lower() == 'vd':
        bot.send_message(message.chat.id, 'Название диода', reply_markup=keyboard_size_res)


# https://mastergroosha.github.io/telegram-tutorial/
# https://habr.com/ru/users/dimagorovtsov/posts/
# https://python-telegram-bot.readthedocs.io/en/stable/telegram.html
# https://habr.com/ru/post/442800/
bot.polling()
