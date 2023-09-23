import telebot
from telebot import types

bot = telebot.TeleBot('6396799144:AAFSIsMLN8rqL-vAAmp8Nnviw6tFy3bHrVc')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    bth1 = types.KeyboardButton('😀 Купить')
    bth2 = types.KeyboardButton('Удалить')
    bth3 = types.KeyboardButton('Пока')

    markup.add(bth1)
    markup.add(bth2, bth3)

    bot.send_message(message.chat.id, '<b>Привет!</b> <em>Добро пожаловать в нашего TG бота!</em>', parse_mode='html')

    with open('15780024-1.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f, caption='lu41k', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == '😀 Купить':
        with open('15780024-1.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f, caption='lu41k')

    elif message.text == 'Удалить':
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Успешно удалено!')

bot.polling(non_stop=True)
