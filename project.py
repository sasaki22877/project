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
               types.InlineKeyboardButton(text='Тренировки', callback_data='btn4'),
               types.InlineKeyboardButton(text='Карьера', callback_data='btn5'),
               types.InlineKeyboardButton(text='Ещё', callback_data='btn6'))

        bot.send_message(callback.message.chat.id, 'Выберите действие.', reply_markup=kb)

    elif callback.data == 'btn2':
        bot.send_message(callback.message.chat.id, 'До скорых встреч. Удачи!')

    elif callback.data == 'btn3':
        kb = types.InlineKeyboardMarkup(row_width=2)

        kb.add(types.InlineKeyboardButton(text='Математика', callback_data='btn7'),
               types.InlineKeyboardButton(text='Русский язык', callback_data='btn8'),
               types.InlineKeyboardButton(text='Информатика', callback_data='btn9'),
               types.InlineKeyboardButton(text='Физика', callback_data='btn10'))

        bot.send_message(callback.message.chat.id, 'Выберите предмет для изучения:', reply_markup=kb)


    if callback.data == 'btn7': # Математика
        bot.send_message(callback.message.chat.id, f'Перейдите по ссылке: {youtube_video}')
        bot.send_message(callback.message.chat.id, 'Удачи в изучении!')
        
    if callback.data == 'btn8': #Русский 
        bot.send_message(callback.message.chat.id, 'Какую тему вы бы хотели пройти?')

    if callback.data == 'btn9': # Информатика
        bot.send_message(callback.message.chat.id, 'Пожалуйста, напишите ваш класс обучения в формате числа.')
        
    @bot.message_handler(func=lambda message: True)  # Handler for any message
    def echo_all(message):
        if message.text == '9':
            bot.send_message(callback.message.chat.id, f'Приятного обучения {youtube_inf1}')
        
        elif message.text == '10':
            bot.send_message(callback.message.chat.id, f'Приятного обучения {youtube_inf2}')
        
        elif message.text == '11':
            bot.send_message(callback.message.chat.id, f'Приятного обучения {youtube_inf3}')
        
        else:
            bot.send_message(callback.message.chat.id, "Извини, я не понимаю твоего сообщения.")
    
    if callback.data == 'btn10': # Физика
        kb = types.InlineKeyboardMarkup(row_width=2)

        kb.add(types.InlineKeyboardButton(text='Выслать', callback_data='btn11'))
        
        bot.send_message(callback.message.chat.id, 'Мы можем выслать вам файл с формулами по физике.')

    def send_file(chat_id, file_path):
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id, file)

    # обработчик кнопки
    @bot.callback_query_handler(func=lambda call: call.data == 'btn11')
    def handle_callback_query(callback):
        chat_id = callback.message.chat.id  # куда нужно отправить файл
        file_path = 'Новый/Пользователи/ryu8777/Загрузки/phys.pdf'  # Путь к файлу
        send_file(chat_id, file_path)



try:
    bot.infinity_polling()
    # bot.polling(non_stop = True, interval = 0)
except Exception as e:
    pass
