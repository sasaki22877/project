import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace 'YOUR_BOT_TOKEN' with the actual token you received from BotFather
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Handler for the '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Watch YouTube Video", callback_data="youtube"))

    bot.send_message(user_id, "Click the button below to watch a YouTube video:", reply_markup=markup)

# Handler for the button click event
@bot.callback_query_handler(func=lambda call: call.data == "youtube")
def send_youtube_video(call):
    user_id = call.message.chat.id
    video_url = "https://www.youtube.com/watch?v=VIDEO_ID"  # Replace VIDEO_ID with the actual YouTube video ID
    bot.send_message(user_id, f"Here's the YouTube video you requested:\n{video_url}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
