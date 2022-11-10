import telebot
from telebot import types
import config
import time

# Не забудьте подставить свой токен!
token = '5693586989:AAHO24PzcB6IKQSDNuSncS9T3CX5_x3HTBE'
bot = telebot.TeleBot(token)
TO_CHAT_ID =  -1001848377879

def telegram_bot():
    @bot.message_handler(commands=['start'])
    def send_welcome(message: types.Message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Конкурси')
        item2 = types.KeyboardButton("Задай питання профкому")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Привіт хайовце, тебе вітає Профспілка студентів ХАІ ✌️ ",  reply_markup=markup)

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
            #bot.send_message(message.chat.id, "Анонс конкурсу буде найближчим часом❤\n"
            #                                  "Слідкуй за новинами в наших соціальних мережах:\n"
            #                                  "Instagram(https://instagram.com/profcomkhai?utm_medium=copy_li)\n"
            #                                  "Telegram (https://t.me/profcom_xai)")
            bot.send_message(message.chat.id, "Друже, скоріше надсилай свою найкрутішу фотографію, яка\n"
                                              "була зроблена у період активного студентського життя, та\n"
                                              "розповідай свою цікаву, кумедну або милу історію та обставини, \n"
                                              "за яких виникло це фото 🤪")
            time.sleep(1)
            bot.send_message(message.chat.id, "Перейдемо до умов:🔥\n"
                                              "1. Надіслати історію з фото у бот ХАІ (за посиланням у шапці профілю) і ОБОВ’ЯЗКОВО написати:\n"
                                              "- ПІБ учасника;\n"
                                              "- факультет;\n"
                                              "- нік в інстаграмі.\n\n"
                                              "‼️Зверніть увагу‼️ Не можна:\n\n"
                                              "- ображати чи принижувати будь-кого;\n"
                                              "- нецензурно висловлюватися (можете замінювати іншими смішними словами)));\n"
                                              "- торкатися теми алкоголю, тютюнових чи наркотичних виробів.\n\n")
            time.sleep(2)
            bot.send_message(message.chat.id, "Я вірю в тебе! Успіхів💪")
            bot.register_next_step_handler(message, reply_to_foto)
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
