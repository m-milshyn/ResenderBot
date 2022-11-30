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
        elif(event_name == 'Новорічнийчелендж'):
            merry_christmas(message)
        elif(event_name == 'ПитанняПрофкому'):
            question(message)

    def merry_christmas(message):
        global event_name
        if ((message.text != 'Конкурси')
                and (message.text != 'Головне меню')
                and (message.text != 'Задай питання профкому')
                and (message.text != 'Новорічний челендж')
                and (message.text != 'СТОП')):
            bot.send_message(TO_CHAT_ID, '#Новорічнийчелендж')
            event_name = 'Новорічнийчелендж'
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
                and (message.text != 'Новорічний челендж')
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
            btn1 = types.KeyboardButton('Новорічний челендж')
            btn2 = types.KeyboardButton('Головне меню')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "Конкурси, що тривають:\n    1. Новорічний челендж", reply_markup=markup)
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
        elif (message.text == 'Новорічний челендж'):
            bot.send_message(message.chat.id, "Друзі, вітаємо Вас з початком зими ❄️🤍\n\n"
                                              "Зараз ми як ніколи мріємо про різдвяні дива🙏✨\n"
                                              "Тому ми підготували для вас дещо цікаве 🤪\n\n"
                                              "🎄НОВОРІЧНИЙ ЧЕЛЕНДЖ для хайооовців🎄\n\n"
                                              "Кожного дня у сторіз Ви знайдете круті завдання і ідеї, "
                                              "які точно створять святковий настрій і надихнуть на прекрасні справи✨\n\n"
                                              "Якщо виконуєш завдання, обов'язково показуй це у своїх сторіз з відміткою @profcomkhai, "
                                              "або відправляй у повідомлення цього бота \n\n"
                                              "‼ПРАВИЛА ПОДАЧІ ЗАЯВКИ НА УЧАСТЬ‼\n\n"
                                              "1. Фотографія виконаного завдання\n"
                                              "2. День(що був позначений у сторі), за який ви виконували завдання\n"
                                              "3. ПІБ, номер групи\n"
                                              "4. Нік в інстаграмі")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton('СТОП')
            markup.add(btn)
            bot.send_message(message.chat.id, 'Щоб завершити подачу заявки натисніть на кнопку "СТОП"', reply_markup=markup)
            bot.register_next_step_handler(message, merry_christmas)
    bot.polling(none_stop=True)

def main():
    telegram_bot()

if __name__ == '__main__':
    main()
