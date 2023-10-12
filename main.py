#Импорт необходимой библиотеки
import telebot

#API Токен
bot=telebot.TeleBot("6303605467:AAGxCFTmn8XSh4YBdYNbZQ3YhpQPFxUgc4Q")

#Эксперементальная часть, она не работает
bot.get_chat(chat_id: int) --> Chat
bot.get_state(user_id: int, chat_id: int = None) --> State
#-=========================================================-

#Сообщение при запуске бота командой /start
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Привет, если ты видишь это сообщение, значит бот успешно запущен и работает!(но могут быть проблемы с работой некоторых функций, этого никто не отменял)")

#Копирование сообщения(пока не работает, не реализовано)
@bot.message_handler
def send (message):
    bot.copy_message(chat_id: int, from_chat_id: int, message_id: int)
#-====================================================================-

#Строка для постоянной работы бота 
bot.infinity_polling()
