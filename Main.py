import telebot
import config

bot = telebot.TeleBot(config.token)

keyboard_start = telebot.types.ReplyKeyboardMarkup(True)
keyboard_start.row('Добавить', 'Удалить', 'Найти')
keyboard_add = telebot.types.ReplyKeyboardMarkup(True)
keyboard_add.row('R', 'C', 'VD', 'VT', 'DC/DC')
keyboard_size_res = telebot.types.ReplyKeyboardMarkup(True)
keyboard_size_res.row('0402', '0603', '0805', '1206', '1210', '2010', '2512')
keyboard_size_cap = telebot.types.ReplyKeyboardMarkup(True)
keyboard_size_cap.row('0402', '0603', '0805').row('1206', '1210', '2010', '2512').add('Эл-лит', 'Керамика', 'Плёнка')
keyboard_perc = telebot.types.ReplyKeyboardMarkup(True)
keyboard_perc.row('1%', '5%')

a=[]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, выбери действие /start', reply_markup=keyboard_start)
    bot.register_next_step_handler(message, send_question_element)

@bot.message_handler(text=['Добавить'])
def send_question_element(message):
    a.append(message.text)
    bot.send_message(message.chat.id, 'Какой элем?', reply_markup=keyboard_add)
    bot.send_message(message.chat.id, a, reply_markup=keyboard_add)
 #       bot.register_next_step_handler(message, send_question_size_add)
@bot.message_handler(text=['Удалить'])
#    elif message.text.lower() == 'удалить':
def send_question_element(message):
    a.append(message.text)
    bot.send_message(message.chat.id,'Какой', reply_markup=keyboard_add)
    bot.send_message(message.chat.id, a, reply_markup=keyboard_add)
#        bot.register_next_step_handler(message, send_question_size_add)

#    elif message.text.lower() == 'найти':
#        bot.send_message(message.chat.id, 'элемент', reply_markup=keyboard_add)
#        bot.register_next_step_handler(message, send_question_size_add)

"""
def send_question_size_add(message):
    if message.text.lower() == 'r':
        a.append(message.text)
        bot.send_message(message.chat.id, 'Типоразмер?', reply_markup=keyboard_size_res)
#        bot.register_next_step_handler(message, send_question_percent)

    elif message.text.lower() == 'c':
        bot.send_message(message.chat.id, 'Типоразмер или вид', reply_markup=keyboard_size_cap)
#        bot.register_next_step_handler(message, send_question_percent)

    elif message.text.lower() == 'vd':
        bot.send_message(message.chat.id, 'Название диода', reply_markup=keyboard_size_res)
 #       bot.register_next_step_handler(message, send_question_percent)

def send_question_percent(message):
    a.append(message.text)
    if message.text.lower() == '0402':
        bot.send_message(message.chat.id, 'Процентаж?', reply_markup=keyboard_perc)
        bot.register_next_step_handler(message, send_question_nominal)
    elif message.text.lower() == '0603':
        bot.send_message(message.chat.id, 'Процентаж?', reply_markup=keyboard_perc)
        bot.register_next_step_handler(message, send_question_nominal)

def send_question_nominal(message):
    a.append(message.text)
    if message.text.lower() == '1%':
        bot.send_message(message.chat.id, 'Номинал?', reply_markup=keyboard_perc)
        bot.register_next_step_handler(message, send_question_apply)
    elif message.text.lower() == '5%':
        bot.send_message(message.chat.id, 'Номинал?', reply_markup=keyboard_perc)
        bot.register_next_step_handler(message, send_question_apply)

def send_question_apply(message):
    if message.text.lower() == 'yes':
        bot.send_message(message.chat.id, a, reply_markup=keyboard_perc)
    elif message.text.lower() == 'no':
        bot.send_message(message.chat.id, 'Номинал?', reply_markup=keyboard_perc)
"""

# https://mastergroosha.github.io/telegram-tutorial/
# https://habr.com/ru/users/dimagorovtsov/posts/
# https://python-telegram-bot.readthedocs.io/en/stable/telegram.html
# https://habr.com/ru/post/442800/
bot.polling()
