# подкючение библиотеки telebot
import telebot
from telebot import types
from config import *

# токен
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    # создание кнопок
    kb = types.InlineKeyboardMarkup(row_width=2)
    bt1 = types.InlineKeyboardButton(text='Начать работу', callback_data='btn1')
    bt2 = types.InlineKeyboardButton(text='Закончить работу', callback_data='btn2')
    kb.add(bt1, bt2)
    # вывод сообщения с кнопками
    bot.send_message(message.chat.id, f'Здравствуйте. Начать работу?', reply_markup=kb)


# отслеживание нажатия кнопок
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        kb = types.InlineKeyboardMarkup(row_width=2)

        kb.add(types.InlineKeyboardButton(text='Учеба', callback_data='btn3'),
               types.InlineKeyboardButton(text='Тренировки', callback_data='btn4'))

        kb.add(types.InlineKeyboardButton(text='Карьера', callback_data='btn5'),
               types.InlineKeyboardButton(text='Ещё', callback_data='btn6'))

        bot.send_message(callback.message.chat.id, 'Выберите действие.', reply_markup=kb)

    elif callback.data == 'btn2':
        bot.send_message(callback.message.chat.id, 'До скорых встреч. Удачи!')

    elif callback.data == 'btn3':
        kb = types.InlineKeyboardMarkup(row_width=2)

        kb.add(types.InlineKeyboardButton(text='Математика', callback_data='btn7'),
               types.InlineKeyboardButton(text='Русский язык', callback_data='btn8'))

        kb.add(types.InlineKeyboardButton(text='Информатика', callback_data='btn9'),
               types.InlineKeyboardButton(text='Физика', callback_data='btn10'))

        bot.send_message(callback.message.chat.id, 'Выберите предмет для изучения:', reply_markup=kb)

    elif callback.data == 'btn8':
        bot.send_message(callback.message.chat.id, 'Какую тему вы бы хотели пройти?')

    elif callback.data == 'btn7':
        bot.send_message('Перейдите по ссылке:', youtube_video)
        bot.send_message(callback.message.chat.id, 'Удачи в изучении!')

    elif callback.data == 'btn9':
        bot.send_message(callback.message.chat.id, 'Пожалуйста, напишите ваш класс обучения в формате числа.')
        def echo_all(message):
            if message.text.lower() == '9':
                    bot.reply_to(callback.message.chat.id, "Приятного обучения", youtube_inf1)
            elif message.text.lower() == '10':
                    bot.reply_to(callback.message.chat.id, "Приятного обучения", youtube_inf2)
            elif message.text.lower() == '11':
                    bot.reply_to(callback.message.chat.id, "Приятного обучения", youtube_inf3)
    else:
        bot.reply_to(callback.message.chat.id, "Извини, я не понимаю твоего сообщения.")



if __name__ == "__main__":
    bot.polling(none_stop=True)