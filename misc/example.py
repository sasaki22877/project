import time
import telebot
import config

bot = telebot.TeleBot(config.token)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Чтобы получить ваши материалы с МК нажмите /get_mk1')

# Register command
@bot.message_handler(commands=['register'])
def register(message):

    bot.send_message(message.chat.id,f'Ура!👍 Вы зарегистрированы 😘')
    bot.send_message(message.chat.id,f'Теперь вы можете скачать приветственный рецепт по ссылке: http://agraphena3.ru/welcome/recipe.pdf')
    bot.send_message(message.chat.id,f'Бот будет присылать новый рецепт, которым я пользуюсь в своей работе, каждые 2-3 дня')
    bot.send_message(message.chat.id, f'Чтобы получить ваши материалы с МК нажмите /get_mk1')

# Button1 command
@bot.message_handler(commands=['get_mk1'])
def button1(message):
    bot.send_message(message.chat.id, 'Введите пароль:')

# Password command
@bot.message_handler(content_types=['text'])
def password(message):
    if message.text == config.password:
        bot.send_message(message.chat.id, 'Ваши материалы с Мастер Класса 😍')
        bot.send_message(message.chat.id,f'Макарон на французской меренге: http://agraphena3.ru/files_mk1/agraphena_macaron_fr.pdf')
        time.sleep(0.01)
        bot.send_message(message.chat.id,f'Макарон на итальянской меренге: http://agraphena3.ru/files_mk1/agraphena_macaron_it.pdf')
        bot.send_message(message.chat.id,f'Макарон на швейцарской меренге: http://agraphena3.ru/files_mk1/agraphena_macaron_sw.pdf')
        bot.send_message(message.chat.id,f'Начинки для Макарон: http://agraphena3.ru/files_mk1/agraphena_macaron_nachinki.pdf')
        bot.send_message(message.chat.id,f'Начинки с МК для Макарон: http://agraphena3.ru/files_mk1/agraphena_nachinki_mk.pdf')
        bot.send_message(message.chat.id,f'Трафареты: http://agraphena3.ru/files_mk1/trafarets.zip')
        bot.send_message(message.chat.id,f'Жду на следующих мастер-классах 🥰🥰🥰')
    else:
        bot.send_message(message.chat.id, 'Неправильный пароль. Повторите снова:')

try:
    bot.infinity_polling()
    # bot.polling(non_stop = True, interval = 0)
except Exception as e:
    pass