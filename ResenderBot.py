import telebot
import time


# Не забудьте подставить свой токен!
token = '5693586989:AAHO24PzcB6IKQSDNuSncS9T3CX5_x3HTBE'
bot = telebot.TeleBot(token)
TO_CHAT_ID = 334372042       # Не забудьте подставить нужный id!

def telegram_bot():
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Привіт ✌️ ")
        time.sleep(2)
        bot.send_message(message.chat.id, "Вітаю зі святом, любий хайовце! Скоріше бери участь у наших мега-конкурсах і вигравай круті призи🤩❤️")
        time.sleep(5)
        bot.send_message(message.chat.id, "Надсилайте 1 або декілька своїх фотографій, які були зроблені у студентський період та розкажіть цікаву, "
                                          "кумедну історію, та за яких обставин виникло це фото. Обов'язково підпишіть історію своїм ніком в інстаграмі, "
                                          "без цієї ви не будете мати права участі у конкурсі.")
        time.sleep(5)
        bot.send_message(message.chat.id, "Хай щастить!☺")

    @bot.message_handler(content_types=["text", "audio", "photo", "video", "voice", "sticker"])
    def all_messages(message):
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)

    bot.polling(none_stop=True)

def main():
    telegram_bot()

if __name__ == '__main__':
    main()
