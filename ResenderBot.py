import telebot
from telebot import types
import config
import time

# Не забудьте подставить свой токен!
token = '5693586989:AAHO24PzcB6IKQSDNuSncS9T3CX5_x3HTBE'
bot = telebot.TeleBot(token)
TO_CHAT_ID =   334372042


def telegram_bot():
    @bot.message_handler(commands=['start'])
    def send_welcome(message: types.Message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Конкурси')
        item2 = types.KeyboardButton("Задай питання профкому")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Привіт ✌️ ",  reply_markup=markup)

    def reply_to_meme(message):
        if ((message.text != 'Конкурси') and (message.text != 'Меми') and (message.text != 'Історія одного фото') and (
                message.text != 'Головне меню') and (message.text != 'Задай питання профкому')):
            bot.send_message(TO_CHAT_ID, '#КонкурсМеми')
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.send_message(message.chat.id, 'Ваша заявка прийнята🫶🏼\n'
                                              'Хай щастить 💓')
        else:
            func(message)
    def reply_to_foto(message):
        if ((message.text != 'Конкурси') and (message.text != 'Меми') and (message.text != 'Історія одного фото') and (
                message.text != 'Головне меню') and (message.text != 'Задай питання профкому')):
            bot.send_message(TO_CHAT_ID, '#КонкурсІсторіяОдногоФото')
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.send_message(message.chat.id, 'Ваша заявка прийнята🫶🏼\n'
                                              'Хай щастить 💓')
        else:
            func(message)
    def reply_to_question(message):
        if ((message.text != 'Конкурси') and (message.text != 'Меми') and (message.text != 'Історія одного фото') and (message.text != 'Головне меню') and (message.text != 'Задай питання профкому')):
            bot.send_message(TO_CHAT_ID, '#ПитанняПрофкому')
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.send_message(message.chat.id, 'Дякуємо за ваше питання')
        else:
            func(message)

    @bot.message_handler(content_types=['text', "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"])
    def func(message):
        if message.text == 'Конкурси':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Меми')
            btn2 = types.KeyboardButton('Історія одного фото')
            btn3 = types.KeyboardButton('Головне меню')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Вибери який конкурс тебе цікавить: ', reply_markup=markup)
        elif (message.text == 'Меми'):
            message = bot.send_message(message.chat.id, 'Що треба зробити для участі в цьому конкурсі:\n'
                                              '1. Зробити мем у фото чи відео (тік ток) форматі.\n\n'
                                              '❗️Зверніть увагу❗️Не можна:\n'
                                              '- жартувати про викладачів і працівників закладу;\n'
                                              '- ображати чи принижувати будь-кого;\n'
                                              '- нецензурно висловлюватися;\n'
                                              '- використовувати у відео/ жартувати на тему алкоголю, тютюнових чи наркотичних виробів;\n'
                                              '- піднімати політичні питання, що сприяють розпалюванню конфліктів.\n\n'
                                              '2. Надіслати відео/фото у бот ХАІ (за посиланням у шапці профілю) і ОБОВ’ЯЗКОВО написати:\n'
                                              '- ПІБ учасника;\n'
                                              '- Ваш факультет;\n'
                                              '- нік в інстаграмі.')
            bot.register_next_step_handler(message, reply_to_meme)
        elif (message.text == 'Історія одного фото'):
            bot.send_message(message.chat.id, "Анонс конкурсу буде найближчим часом❤\n"
                                              "Слідкуй за новинами в наших соціальних мережах:\n"
                                              "Instagram(https://instagram.com/profcomkhai?utm_medium=copy_li)\n"
                                              "Telegram (https://t.me/profcom_xai)")
            #bot.send_message(message.chat.id, "Надсилайте 1 або декілька своїх фотографій, які були зроблені у студентський період та розкажіть цікаву, "
            #                                  "кумедну історію, та за яких обставин виникло це фото. Обов'язково підпишіть історію своїм ніком в інстаграмі, "
            #                                  "без цієї ви не будете мати права участі у конкурсі.")
            #time.sleep(3)
            #bot.send_message(message.chat.id, "Хай щастить!☺")
            #bot.register_next_step_handler(message, reply_to_foto)
        elif (message.text == 'Головне меню'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Конкурси')
            item2 = types.KeyboardButton("Задай питання профкому")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Головне меню:", reply_markup=markup)
        elif (message.text == 'Задай питання профкому'):
            bot.send_message(message.chat.id, "Напишіть своє питання, та обов'язково в кінці "
                                              "укажіть свої контактні дані(ПІБ, номер групи, номер телефону, telegram або instagram)")
            bot.register_next_step_handler(message, reply_to_question)
    bot.polling(none_stop=True)



def main():
    telegram_bot()

if __name__ == '__main__':
    main()
