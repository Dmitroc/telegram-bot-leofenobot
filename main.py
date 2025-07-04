import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")  # Токен берётся из переменной окружения

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Бот запущен и готов к работе.")

print("⚙️ Бот запускается...")

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"❌ Ошибка запуска бота: {e}")
