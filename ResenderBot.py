import telebot
from telebot import types
import config
import time

# Не забудьте подставить свой токен!
token = '5693586989:AAHO24PzcB6IKQSDNuSncS9T3CX5_x3HTBE'
bot = telebot.TeleBot(token)
TO_CHAT_ID =  -1001848377879
event_name = ''

def telegram_bot():
    @bot.message_handler(commands=['start'])
    def send_welcome(message: types.Message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Конкурси')
        item2 = types.KeyboardButton("Задай питання профкому")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Привіт хайовце, тебе вітає Профспілка студентів ХАІ ✌️ ",  reply_markup=markup)

    def forward_messsage(message):
        global event_name
        if(message.text != 'СТОП'):
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(message, forward_messsage)
        elif(event_name == 'Фотоконкурсдо8березня'):
            march_8(message)
        elif(event_name == 'ПитанняПрофкому'):
            question(message)

    def march_8(message):
        global event_name
        if ((message.text != 'Конкурси')
                and (message.text != 'Головне меню')
                and (message.text != 'Задай питання профкому')
                and (message.text != 'Фотоконкурс до 8 березня')
                and (message.text != 'СТОП')):
            bot.send_message(TO_CHAT_ID, '#Фотоконкурсдо8березня')
            event_name = 'Фотоконкурсдо8березня'
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(message, forward_messsage)
        else:
            bot.send_message(message.chat.id, 'Ваша заявка прийнята🫶🏼\nХай щастить 💓')
            func(message)

    def question(message):
        global event_name
        if ((message.text != 'Конкурси')
                and (message.text != 'Головне меню')
                and (message.text != 'Задай питання профкому')
                and (message.text != 'Фотоконкурс до 8 березня')
                and (message.text != 'СТОП')):
            bot.send_message(TO_CHAT_ID, '#ПитанняПрофкому')
            event_name = 'ПитанняПрофкому'
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(message, forward_messsage)
        else:
            bot.send_message(message.chat.id, 'Дякуємо за ваше питання')
            func(message)

    @bot.message_handler(content_types=['text', "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"])
    def func(message):
        if message.text == 'Конкурси':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Фотоконкурс до 8 березня')
            btn2 = types.KeyboardButton('Головне меню')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "Конкурси, що тривають:\n    1. Фотоконкурс до 8 березня", reply_markup=markup)
        elif (message.text == 'Головне меню') or (message.text == 'СТОП'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Конкурси')
            item2 = types.KeyboardButton("Задай питання профкому")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Головне меню:", reply_markup=markup)
        elif (message.text == 'Задай питання профкому'):
            bot.send_message(message.chat.id, "Напишіть своє питання та обов'язково в кінці "
                                              "залиште свої контактні дані(ПІБ, номер групи, номер телефону, telegram або instagram)")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton('СТОП')
            markup.add(btn)
            bot.send_message(message.chat.id, 'Щоб завершити подачу заявки натисніть на кнопку "СТОП"',
                             reply_markup=markup)
            bot.register_next_step_handler(message, question)
        elif (message.text == 'Фотоконкурс до 8 березня'):
            bot.send_message(message.chat.id, "❗ATTENTION❗\n"
                                              "Необхідно надіслати свою історію у бот Профкому студентів "
                                              "ХАІ  або в дірект нашого інстаграму і ОБОВ’ЯЗКОВО написати:\n"
                                              "✅ПІБ учасника;\n"
                                              "✅факультет;\n"
                                              "✅нік в інстаграмі.\n\n"
                                              "Конкурс триватиме з 08.03.2023 до 15.03.2023 (20.00).\n\n"
                                              "Переможця оберуть студенти в сторіс у інстаграмі @profcomkhai\n"
                                              "❗16.03.2023 з 8.00 до 20.00.❗")
            bot.send_message(message.chat.id, "Якщо ви хочете відправити більше 1 фото, то будь-ласка, відправляйте їх по одному. "
                                              "Групи фотографій прийматися не будуть!")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton('СТОП')
            markup.add(btn)
            bot.send_message(message.chat.id, 'Щоб завершити подачу заявки натисніть на кнопку "СТОП"', reply_markup=markup)
            bot.register_next_step_handler(message, march_8)
    bot.polling(none_stop=True)

def main():
    telegram_bot()

if __name__ == '__main__':
    main()
