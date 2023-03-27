import telebot
from telebot import types

token = '5693586989:AAHO24PzcB6IKQSDNuSncS9T3CX5_x3HTBE'
bot = telebot.TeleBot(token)
TO_CHAT_ID = -1001848377879
dev_chat_id = 1436890435
event_name = ""
check_num = False


def telegram_bot():
    @bot.message_handler(commands=["start"])
    def send_welcome(message: types.Message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(types.KeyboardButton("Конкурси"),
                   types.KeyboardButton("Положення"),
                   types.KeyboardButton("Реквізити"),
                   types.KeyboardButton("Задай питання профкому"),
                   types.KeyboardButton("Повідомити про технічну помилку"),
                   types.KeyboardButton("Пропозиції та скарги"),
                   types.KeyboardButton("Зв’язок з деканатом та соціальні мережі"),
                   types.KeyboardButton("Питання/відповідь"),
                   types.KeyboardButton("Профбюро студентів та департаменти ППОС НАУ \"ХАІ\""))
        chat_message = "Обери пункт, який тобі необхіден"
        bot.send_message(message.chat.id, "Привіт, хайовець!\n"
                                          "Тебе вітає Профком студентів ХАІ! ✌️ ")
        bot.send_message(message.chat.id, chat_message, reply_markup=markup)

    def check(message):
        if ((message.text != "Конкурси")
                and (message.text != "Головне меню")
                and (message.text != "Задай питання профкому")
                and (message.text != "Міс ХАІ: етап факультет")
                and (message.text != "Повідомити про технічну помилку")
                and (message.text != "Зв’язок та соціальні мережі")
                and (message.text != "Пропозиції Та Скарги")
                and (message.text != "Профбюро студентів та департаменти ППОС НАУ \"ХАІ\"")
                and (message.text != "СТОП")):
            return True
        else:
            return False

    def handle_1_faculty(message):
        chat_message = "1 факультет\n\n" \
                       "Профспілкове бюро студентів факультету №1 - це структурний елемент профспілки студентів," \
                       "головною метою якого є спрямованість на захист прав студентів та створення умов для їхньої самореалізації.\n\n" \
                       "Головою Профбюро студентів факультету №1 є Мільшин Микита Сергійович @milshyn_mykyta"
        bot.send_message(message.chat.id, chat_message)

    def handle_2_faculty(message):
        chat_message = "2 факультет\n\n" \
                       "Профспілкове бюро студентів факультету №2 - це структурний елемент профспілки студентів, " \
                       "головною метою якого є спрямованість на захист прав студентів та створення умов для їхньої самореалізації.\n\n" \
                       "В. о. голови Профбюро студентів факультету №2 є Марчук Єлизавета Миколаївна @lizamarchuk"
        bot.send_message(message.chat.id, chat_message)

    def handle_3_faculty(message):
        chat_message = "3 факультет\n\n" \
                       "Профспілкове бюро студентів факультету №3 - це структурний елемент профспілки студентів, " \
                       "головною метою якого є спрямованість на захист прав студентів та створення умов для їхньої самореалізації.\n\n" \
                       "Головою Профбюро студентів факультету №3 є Бєлашов Артем Ігорович @Shushuku"
        bot.send_message(message.chat.id, chat_message)

    def handle_4_faculty(message):
        chat_message = "4 факультет\n\n" \
                       "Профспілкове бюро студентів факультету №4 - це структурний елемент профспілки студентів, " \
                       "головною метою якого є спрямованість на захист прав студентів та створення умов для їхньої самореалізації.\n\n" \
                       "Головою Профбюро студентів факультету №4 є Левченко Михайло Андрійович @Misha_TyTa"
        bot.send_message(message.chat.id, chat_message)

    def handle_5_faculty(message):
        chat_message = "5 факультет\n\n" \
                       "Профспілкове бюро студентів факультету №5 - це структурний елемент профспілки студентів, " \
                       "головною метою якого є спрямованість на захист прав студентів та створення умов для їхньої самореалізації.\n\n" \
                       "В. о. голови Профбюро студентів факультету №5 є Літвінов Андрій Андрійович @Andreoyne"
        bot.send_message(message.chat.id, chat_message)

    def handle_6_faculty(message):
        chat_message = "6 факультет\n\n" \
                       "Профспілкове бюро студентів факультету №6 - це структурний елемент профспілки студентів, " \
                       "головною метою якого є спрямованість на захист прав студентів та створення умов для їхньої самореалізації.\n\n" \
                       "Головою Профбюро студентів факультету №6 є Дикун Діана Валеріївна @dixxxdiii"
        bot.send_message(message.chat.id, chat_message)

    def handle_7_faculty(message):
        chat_message = "7 факультет\n\n" \
                       "Профспілкове бюро студентів факультету №7 - це структурний елемент профспілки студентів, " \
                       "головною метою якого є спрямованість на захист прав студентів та створення умов для їхньої самореалізації.\n\n" \
                       "Головою Профбюро студентів факультету №7 є Байрамова Регіна Рамізівна @regi_san"
        bot.send_message(message.chat.id, chat_message)

    def handle_8_faculty(message):
        chat_message = "8 факультет\n\n" \
                       "Профспілкове бюро студентів факультету №8 - це структурний елемент профспілки студентів, " \
                       "головною метою якого є спрямованість на захист прав студентів та створення умов для їхньої самореалізації.\n\n" \
                       "В. о. голови Профбюро студентів факультету №8 є Павленко Оксана Олександрівна @Pavlenko_15"
        bot.send_message(message.chat.id, chat_message)

    def handle_KMIP(message):
        chat_message = "Де КМІП\n\n" \
                       "Департамент культурно-масових та іміджевих проектів комітету первинної профспілкової організації студентів ХАІ " \
                       "є одним з найважливіших департаментів структури. Члени департаменту КМІП займаються організацією культурного дозвілля студентів, " \
                       "проведенням громадських заходів факультетів та ВНЗ, сприяють інтелектуальному і культурному збагаченню студентства.\n\n" \
                       "Головою департаменту культурно-масових та іміджевих проектів є Жукова Єлизавета Олегівна @xmlkwx"
        bot.send_message(message.chat.id, chat_message)

    def handle_MK(message):
        chat_message = "Де МК\n\n" \
                       "Робота департаменту медіа-комунікацій є однією з найважливіших видів діяльності профкому студентів. " \
                       "Члени департаменту МК відповідають за донесення актуальної інформації до студентів. Основним напрямком " \
                       "роботи є збір та аналіз інформації, яка надалі доноситися до студентів.\n\n" \
                       "Головою департаменту медіа-комунікацій є Тюріна Діана Романівна @dityurina"
        bot.send_message(message.chat.id, chat_message)

    def handle_SO(message):
        chat_message = "Де СО\n\n" \
                       "Департамент сектору обліку займається організацією та проведенням вступу до Профспілки студентів, " \
                       "обліком профквитків та статистикою по ступу до Профспілки студентів.\n\n" \
                       "Головою департаменту сектору обліку є Пасічник Дарина Валентинівна @daryna_pasechnyk"
        bot.send_message(message.chat.id, chat_message)

    def handle_SORTT(message):
        chat_message = "Де СОРТТ\n\n" \
                       "Департамент спортивно-оздоровчої роботи та туризму займається проведенням спортивних заходів на університетському рівні, " \
                       "організацією акцій і різноманітних тренінгів оздоровчого характеру. Основними щорічними змаганнями є турніри з футболу та волейболу, " \
                       "в яких команди-переможці отримують призи, а також мають можливість взяти участь в подальших міських турнірах з уже награним і звичним складом.\n\n" \
                       "Головою департаменту спортивно-оздоровчої роботи та туризму є Чепелевич Альона Ігорівна @reynikraul"
        bot.send_message(message.chat.id, chat_message)

    def handle_SZNR(message):
        chat_message = "Де СЗНР\n\n" \
                       "Департамент соціального захисту та навчально-наукової роботи " \
                       "Профкому студентів ХАІ приходить на допомогу студентам при виникненні складних, " \
                       "спірних ситуацій, що стосуються навчального процесу в університеті. " \
                       "Також склад департаменту добре розбирається в нормативних документах, " \
                       "тому можуть проконсультувати вас з питань соціального захисту\n\n" \
                       "Головою департаменту соціального захисту та навчально-наукової роботи є Уренова Анастасія Сергіївна @madame_la_comtesse"
        bot.send_message(message.chat.id, chat_message)

    def handle_JP(message):
        chat_message = "Де ЖП\n\n" \
                       "Департамент житлово-побутової роботи ППОС ХАІ здійснює організацію профспілкової житлово-побутової роботи " \
                       "в університеті і вирішує поточні питання, які відносяться до його компетенції, відповідно до статутних цілей " \
                       "і завдання Профспілки студентів ХАІ.\n\n" \
                       "Головою департаменту соціального захисту та навчально-наукової роботи є Бондаренко Владислав Сергійович @vs_bond"
        bot.send_message(message.chat.id, chat_message)

    def handle_ORDTM(message):
        chat_message = "Де ОРДТМ\n\n" \
                       "Основне завдання департаменту організаційної роботи, діловодства та моніторингу - кооперування " \
                       "і упорядкування роботи ППОС ХАІ і вирішення поточних питань профспілкової діяльності, оформлення " \
                       "та постійний контроль документації первинної профспілкової організації, соціальний та правовий " \
                       "захист профспілкових активістів, проведення зборів і конференцій, а також навчання активу факультетів.\n\n" \
                       "Головою департаменту організаційної роботи, діловодства та моніторингу є Ковалевська Анна Вікторівна @Ann_Kovalevska\n" \
                       "Заступником голови є Абібулаєв Марлєн Мієдінович @TsumiDe"
        bot.send_message(message.chat.id, chat_message)

    def faculty_profcom(message):
        if message.text == "1 факультет":
            handle_1_faculty(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "2 факультет":
            handle_2_faculty(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "3 факультет":
            handle_3_faculty(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "4 факультет":
            handle_4_faculty(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "5 факультет":
            handle_5_faculty(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "6 факультет":
            handle_6_faculty(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "7 факультет":
            handle_7_faculty(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "8 факультет":
            handle_8_faculty(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "Де КМІП":
            handle_KMIP(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "Де МК":
            handle_MK(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "Де СО":
            handle_SO(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "Де СОРТТ":
            handle_SORTT(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "Де СЗНР":
            handle_SZNR(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "Де ЖП":
            handle_JP(message)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "Де ОРДТМ":
            handle_ORDTM(message)
            bot.register_next_step_handler(message, faculty_profcom)
        else:
            func(message)

    def req_(message):
        if message.text == "Реквізити для сплати навчання":
            rec_message = "Банківські реквізити для оплати за навчання\n" \
                          "IBAN-рахунок:\n" \
                          "UA878201720313271005201004199\n" \
                          "Призначення платежу:\n" \
                          "сплата за навчання ПІБ студента без скорочень , № договору\n\n" \
                          "Відділ контрактів НАУ «ХАІ»:\n" \
                          "тел.: +38 (057) 788-48-86\n" \
                          "ауд. 117 головного корпусу"
            bot.send_message(message.chat.id, rec_message)
            bot.register_next_step_handler(message, req_)
        elif message.text == "Реквізити для сплати проживання":
            rec_message = "Банківські реквізити для оплати за проживання\n" \
                          "IBAN-рахунок:\n" \
                          "UA828201720313251001202017426\n" \
                          "Призначення платежу:\n" \
                          "за проживання у гуртожитку «ХАІ» № номер гуртожитку , ПІБ студента без скорочень"
            bot.send_message(message.chat.id, rec_message)
            bot.register_next_step_handler(message, req_)
        else:
            func(message)

    def question(message):
        global check_num
        global event_name
        if check(message):
            if not check_num:
                bot.send_message(TO_CHAT_ID, "#ПитанняПрофкому")
                event_name = "ПитанняПрофкому"
                check_num = True
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(message, question)
        elif message.text == "СТОП":
            message.text = "Головне меню"
            func(message)

    def problem_report(message):
        global check_num
        global event_name
        if check(message):
            if not check_num:
                bot.send_message(dev_chat_id, "#ПовідомитиПроПомилку")
                event_name = "ПовідомитиПроПомилку"
                check_num = True
            bot.forward_message(dev_chat_id, message.chat.id, message.message_id)
            bot.register_next_step_handler(message, problem_report)
        elif message.text == "СТОП":
            message.text = "Головне меню"
            func(message)

    def suggestions(message):
        global event_name
        global check_num
        if check(message):
            if not check_num:
                bot.send_message(TO_CHAT_ID, "#ПропозиціїТаСкарги")
                event_name = "Пропозиції Та Скарги"
                check_num = True
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
            bot.register_next_step_handler(message, suggestions)
        elif message.text == "СТОП":
            message.text = "Головне меню"
            func(message)

    def social_and_dekanat(message):
        if message.text == "Соціальні мережі ППОС НАУ \"ХАІ\"":
            bot.send_message(message.chat.id, "Наші соціальні мережі:\n"
                                              "[Сайт Профкому студентів ХАІ](https://education.khai.edu/union/schedule/student/)\n"
                                              "[Instagram Профкому студентів ХАІ](https://instagram.com/profcomkhai?utm_medium=copy_li)\n"
                                              "[Telegram Профкому студентів ХАІ](https://t.me/profcom_xai)\n"
                                              "[YouTube Профкому студентів ХАІ](https://www.youtube.com/@user-sq9tl8bf4j)\n"
                                              "[Instagram 1 факультету](https://www.instagram.com/first_khai/)\n"
                                              "[Instagram 2 факультету](https://www.instagram.com/fae_khai/)\n"
                                              "[Instagram 3 факультету](https://www.instagram.com/sula.khai/)\n"
                                              "[Instagram 4 факультету](https://www.instagram.com/faculty4_you/)\n"
                                              "[Instagram 5 факультету](https://www.instagram.com/recsi_khai/)\n"
                                              "[Instagram 6 факультету](https://www.instagram.com/sixfac_khai/)\n"
                                              "[Instagram 7 факультету](https://www.instagram.com/7fac_khai/)\n"
                                              "[Instagram 8 факультету](https://www.instagram.com/faculty_8_khai_/)\n",
                             parse_mode="Markdown")
            bot.register_next_step_handler(message, social_and_dekanat)
        elif message.text == "Зв’язок з деканатами":
            bot.send_message(message.chat.id, """Зв’язок з деканатом

✈️1 Факультет. Факультет літакобудування
Заступник декана 1 та 4 курсу: +380502863008  - Заклінський Сергій Олександрович
Заступник декана 2 та 3 курсу: +380509024530 - Каратанов Олександр Володимирович
З понеділка по п'ятницю з 10:00 до 16:00.

🛩2 Факультет. Факультет авіаційних двигунів
Номер телефону: 0577884200
З понеділка по п'ятницю з 10:00 до 15:00.
0501897838 - Фесенко Ксенія Володимирівна - заст.декана з навчально-виховної роботи

🛰3 Факультет. Факультет систем управління літальними апаратами.
Номер телефону: 0577884300
З понеділка по п'ятницю з 10:00 до 12:30 та з 13:30 до 15:00

🚀4 Факультет. Факультет ракетно-космічної техніки.
Електрона скринька: v.ostapchuk@khai.edu

💻5 Факультет. Факультет радіоелектроніки, комп'ютерних систем та інфокомунікацій.
Номери телефону: 057 778 4500
                                        093 450 0457
                                        096 450 0457
                                        099 450 0457 
З понеділка по п'ятницю з 09:00 до 17:00.

🖥6 Факультет. Факультет програмної інженерії та бізнесу.
Номер телефону: 0660603375

🧰7 Факультет. Гуманітарно-правовий факультет.
Електрона скринька: 7dekanat@khai.edu

🌎8 Факультет. Факультет іноземних громадян.
Спеціаліст деканата - +380 99 624 2421 - Кравченко Ірина
Спеціаліст деканата - +380 50 542 0385 - Анастасія""")
            bot.register_next_step_handler(message, social_and_dekanat)
        else:
            func(message)

    def FAQ(message):
        if message.text == "1":
            bot.send_message(message.chat.id,
                             "Ви маєте змогу написати заяву та подати пакет документів на оформлення соціальної стипендії у будь-який момент. "
                             "Соціальна стипендія буде нараховуватись з моменту написання заяви")
            bot.register_next_step_handler(message, FAQ)
        if message.text == "2":
            bot.send_message(message.chat.id,
                             "[Приклади шаблонів заяв та документів Ви можете знайти на нашому сайті в розділі “Корисні ресурси”](https://education.khai.edu/union/studresources)",
                             parse_mode="Markdown")
            bot.register_next_step_handler(message, FAQ)
        if message.text == "3":
            bot.send_message(message.chat.id,
                             "На жаль, студенти мають змогу отримувати тільки одну стипендію. Або академічну, або соціальну. "
                             "Рекомендуємо Вам оформлювати соціальну стипендію тільки тоді, коли Ви дізнаєтесь "
                             "кінцевий рейтинг на отримання академічної стипендії")
            bot.register_next_step_handler(message, FAQ)
        if message.text == "4":
            bot.send_message(message.chat.id,
                             "Соціальну стипендію необхідно оформлювати раз в семестр. "
                             "Наприклад, якщо 1 семестр курсу закінчився, то в 2 семестрі "
                             "Вам необхідно ще раз писати заяву та подати пакет документів "
                             "на оформлення соціальної стипендії")
            bot.register_next_step_handler(message, FAQ)
        if message.text == "5":
            bot.send_message(message.chat.id,
                             "Соціальні стипендії - це виплата, яку отримують студенти, які мають право на пільги.\n\n"
                             "[Перелік пільгових категорій, які мають право на оформлення соціальної стипендії](https://drive.google.com/file/d/1NJ3IWLqGvoyiw2LfYo21SpIam-d93j5n/view?usp=share_link)\n\n"
                             "Якщо Ви навчаєтесь на бюджеті, маєте підтверджувальні документи вашого статусу,  "
                             "не маєте академічних заборгованостей - то Ви маєте можливість подати до деканату "
                             "необхідний пакет документів на призначення соціальної стипендії!\n\n"
                             "Приклади заяв на соціальні стипендії та перелік всіх необхідних документів можна знайти  "
                             "у [Додатку Б  \"Положення про рейтингове оцінювання\"](https://khai.edu/assets/files/polozhennya/polozhennya-pro-stipendii.pdf).\n\n"
                             "❗️Не стосується здобувачів освіти, які отримують академічну стипендію❗️",
                             parse_mode="Markdown")
            bot.register_next_step_handler(message, FAQ)
        else:
            func(message)

    @bot.message_handler(
        content_types=['text', "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location",
                       "contact",
                       "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                       "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                       "migrate_from_chat_id", "pinned_message"])
    def func(message):
        global check_num
        if message.text == "Конкурси":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Міс ХАІ: етап факультет")
            btn2 = types.KeyboardButton("Головне меню")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                             "Конкурси, що тривають, або будуть проходити незабаром:\n"
                             "    1. Міс ХАІ: етап факультет - активний\n"
                             "    2. Міс ХАІ: етап всеуніверситетський - в розробці",
                             reply_markup=markup)
        elif message.text == "Головне меню":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(types.KeyboardButton("Конкурси"),
                       types.KeyboardButton("Положення"),
                       types.KeyboardButton("Реквізити"),
                       types.KeyboardButton("Задай питання профкому"),
                       types.KeyboardButton("Повідомити про технічну помилку"),
                       types.KeyboardButton("Пропозиції та скарги"),
                       types.KeyboardButton("Зв’язок з деканатом та соціальні мережі"),
                       types.KeyboardButton("Питання/відповідь"),
                       types.KeyboardButton("Профбюро студентів та департаменти ППОС НАУ \"ХАІ\""))
            chat_message = "Головне меню:\n" \
                           "1. Конкурси\n" \
                           "2. Положення\n" \
                           "3. Реквізити\n" \
                           "4. Задай питання профкому\n" \
                           "5. Повідомити про технічну помилку\n" \
                           "6. Пропозиції та скарги\n" \
                           "7. Зв’язок з деканатом та соціальні мережі\n" \
                           "8. Питання/відповідь\n" \
                           "9. Профбюро студентів та департаменти ППОС НАУ \"ХАІ\""
            bot.send_message(message.chat.id, chat_message, reply_markup=markup)
        elif message.text == "Профбюро студентів та департаменти ППОС НАУ \"ХАІ\"":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(types.KeyboardButton("1 факультет"),
                       types.KeyboardButton("2 факультет"),
                       types.KeyboardButton("3 факультет"),
                       types.KeyboardButton("4 факультет"),
                       types.KeyboardButton("5 факультет"),
                       types.KeyboardButton("6 факультет"),
                       types.KeyboardButton("7 факультет"),
                       types.KeyboardButton("8 факультет"),
                       types.KeyboardButton("Де КМІП"),
                       types.KeyboardButton("Де МК"),
                       types.KeyboardButton("Де СО"),
                       types.KeyboardButton("Де СОРТТ"),
                       types.KeyboardButton("Де СЗНР"),
                       types.KeyboardButton("Де ЖП"),
                       types.KeyboardButton("Де ОРДТМ"),
                       types.KeyboardButton("Головне меню"))
            bot.send_message(message.chat.id, "Оберіть профбюро, або департамент, який вас цікавить:",
                             reply_markup=markup)
            bot.register_next_step_handler(message, faculty_profcom)
        elif message.text == "Питання/відповідь":
            check_num = False
            bot.send_message(message.chat.id, "1. Коли я можу оформити соціальну стипендію?\n"
                                              "2. Де я можу знайти приклади шаблонів заяв та документів?\n"
                                              "3. Скільки всього стипендій я можу отримувати?\n"
                                              "4. Як часто необхідно оформлювати соціальну стипендію?\n"
                                              "5. Що таке соціальні стипендії і хто має право на їх оформлення?\n")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
            markup.add(types.KeyboardButton("1"),
                       types.KeyboardButton("2"),
                       types.KeyboardButton("3"),
                       types.KeyboardButton("4"),
                       types.KeyboardButton("5"))
            markup.add(types.KeyboardButton("Головне меню"), row_width=5)
            bot.send_message(message.chat.id, "Оберіть пункт меню, що відповідає порядковому номеру питання:",
                             reply_markup=markup)
            bot.register_next_step_handler(message, FAQ)
        elif message.text == "Пропозиції та скарги":
            check_num = False
            bot.send_message(message.chat.id,
                             "Хайовцю, напиши свою пропозицію чи скаргу та обов'язково в кінці залиште свої контактні дані для отримання зворотного зв’язку:\n"
                             "ПІБ\n"
                             "Номер групи\n"
                             "Номер телефону\n"
                             "Telegram або Instagram\n")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton("СТОП")
            markup.add(btn)
            bot.send_message(message.chat.id, "Щоб завершити подачу заявки натисніть на кнопку \"СТОП\"",
                             reply_markup=markup)
            bot.register_next_step_handler(message, suggestions)
        elif message.text == "Зв’язок з деканатом та соціальні мережі":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("Соціальні мережі ППОС НАУ \"ХАІ\""),
                       types.KeyboardButton("Зв’язок з деканатами"),
                       types.KeyboardButton("Головне меню"))
            bot.send_message(message.chat.id, "Оберіть що Вас цікавить:",
                             reply_markup=markup)
            bot.register_next_step_handler(message, social_and_dekanat)
        elif message.text == "Повідомити про технічну помилку":
            check_num = False
            bot.send_message(message.chat.id, "Шановні хайовці!"
                                              "Якщо ви помітили, що сайт Профкому студентів ХАІ чи система для дистанційного навчання “Ментор” "
                                              "працює некоректно, то прохання повідомити нам.\n\n"
                                              "Щоб це зробити надайте будь-ласка таку інформацію:\n"
                                              "1. ПІБ, номер групи;\n"
                                              "2. Де саме на сайті ви помітили помилку;\n"
                                              "3. Надайте розгорнутий опис проблеми, яку ви помітили.")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton("СТОП")
            markup.add(btn)
            bot.send_message(message.chat.id, "Щоб завершити подачу заявки натисніть на кнопку \"СТОП\"",
                             reply_markup=markup)
            bot.register_next_step_handler(message, problem_report)
        elif message.text == "Положення":
            chat_message = "Положення:\n\n" \
                           "1. [Правила призначення і виплати стипендій здобувачам вищої освіти](https://khai.edu/assets/files/polozhennya/polozhennya-pro-stipendii.pdf)\n" \
                           "2. [Положення про академічну доброчесність](https://khai.edu/assets/files/polozhennya/polozhennya-pro-akademichnu-dobrochesnist.pdf)\n" \
                           "3. [Положення про рейтингове оцінювання досянень студентів](https://khai.edu/assets/files/polozhennya/polozhennya-pro-rejtingove-ocinyuvannya-dosyagnen-studentiv.pdf)\n" \
                           "4. [Про надання державної цільової підтримки деяким категоріям студентів, пов’язаної з проживанням у гутрожитках](https://khai.edu/assets/files/polozhennya/polozhennya-pro-nadannya-derzhavnoi-cilovoi-pidtrimki-studentiv-pov%E2%80%99yazanoi-z-prozhivannyam-u-gurtozhitkah.pdf)\n" \
                           "5. [Положення про навчання здобувачів вищої освіти за індивідуальним графіком](https://khai.edu/assets/files/polozhennya/polozhennya-pro-navchannya-zdobuvachiv-vishhoi-osviti-za-individualnim-grafikom.pdf)\n" \
                           "6. [Графік освітнього процесу ](https://khai.edu/ua/education/grafik-osvitnogo-procesu-2020/2021/denna-forma-navchannya6/)\n" \
                           "7. [Положення про студентський гуртожиток](https://khai.edu/assets/files/polozhennya/polozhennya_gurtozhitki_hai_2015.PDF)\n"
            bot.send_message(message.chat.id, chat_message, parse_mode="Markdown")
        elif message.text == "Реквізити":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(types.KeyboardButton("Реквізити для сплати навчання"),
                       types.KeyboardButton("Реквізити для сплати проживання"),
                       types.KeyboardButton("Головне меню"))
            bot.send_message(message.chat.id, "Оберіть які саме реквізити Вам потрібні:", reply_markup=markup)
            bot.register_next_step_handler(message, req_)
        elif message.text == "Задай питання профкому":
            check_num = False
            bot.send_message(message.chat.id, "Напишіть своє питання та обов'язково в кінці "
                                              "залиште свої контактні дані(ПІБ, номер групи, номер телефону, telegram або instagram)")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton("СТОП")
            markup.add(btn)
            bot.send_message(message.chat.id, "Щоб завершити подачу заявки натисніть на кнопку \"СТОП\"",
                             reply_markup=markup)
            bot.register_next_step_handler(message, question)
        elif message.text == "Міс ХАІ: етап факультет":
            check_num = False
            chat_message = "🎀 Наші любі дівчатка! 🎀\n\n" \
                           "Профком студентів ХАІ має крутецьку новину для вас.🤪\n\n" \
                           "Сьогодні ми розпочинаємо пошуки нашої \"Міс ХАІ 2023\" 🤯" \
                           "Проходити ця масштабна подія буде в два тури. Спочатку обирається міс кожного факультету, а потім дівчата боряться за звання головної дівчини - \"Міс ХАІ 2023\"🏆\n\n" \
                           "[Реєстрація триває до 30.03.2023 до 12.00](https://docs.google.com/forms/d/e/1FAIpQLScu-Jq07SaCeEgbcpdtJUrrIsPW1QAmNZqc-Uh-5IwN5kRRgg/viewform)\n" \
                           "Тож не зволікай, реєструйся та вривайся в двіж разом з нами 👑"
            bot.send_message(message.chat.id, chat_message, parse_mode="Markdown")

    bot.polling(none_stop=True)


def main():
    telegram_bot()


if __name__ == '__main__':
    main()
