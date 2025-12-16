from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, filters
import os
from datetime import datetime, time
TOKEN = os.getenv("BOT_TOKEN")

classi = {
    '5': ['А', 'Б'],
    '6': ['А', 'Б'],
    '7':['А', 'Б','В Е', 'В М'],
    '8': ['А', 'Б','В', 'Г МЭ', 'Г ХБ'],
    '9': ['А ФМ', 'А ФХ','Б','В МЭ','В ХБ'],
    '10':['А','Б','В МЭ','В ХБ'],
    '11':['А','Б МИ','Б ХБ', 'Б ФХ','В','Г']
}

schedule = {
    '5А': 'AgACAgIAAxkBAAPcaTtMkbbOz7XK4jntjlsdizPsnAoAAmUOaxttAtlJ3cRBvjiTsFkBAAMCAAN5AAM2BA',
    '5Б': 'AgACAgIAAxkBAAPdaTtMkRIybjbjMJPFRYtAHWO12qsAAmYOaxttAtlJ2Un_5GMQZVIBAAMCAAN5AAM2BA',
    '6А': 'AgACAgIAAxkBAAPeaTtMkfsBckOLi-G07J9v63xGPFsAAmMOaxttAtlJn1uKvLl8yuoBAAMCAAN5AAM2BA',
    '7А': 'AgACAgIAAxkBAAPfaTtMkao8yQbDiwLqLcReCBQwfuAAAmcOaxttAtlJyhu47wv8HVgBAAMCAAN5AAM2BA',
    '6Б': 'AgACAgIAAxkBAAPgaTtMkUBxL2cJFRONwCi-DH6_heIAAmQOaxttAtlJQVmp6nSdLocBAAMCAAN5AAM2BA',
    '7Б' : 'AgACAgIAAxkBAAPhaTtMkSTQKgJR209-_j3JPudvMGQAAmgOaxttAtlJodYSb37B02EBAAMCAAN5AAM2BA',
    '7В М': 'AgACAgIAAxkBAAPiaTtMkS7fEMKj-M--fAxqS4NrE9oAAmkOaxttAtlJoUFV00P4aosBAAMCAAN5AAM2BA',
    '7В Е': 'AgACAgIAAxkBAAPjaTtMkcWERj4IJt7zEQgFjUiXBecAAmoOaxttAtlJJnZV6wfMcMUBAAMCAAN5AAM2BA',
    '8А': 'AgACAgIAAxkBAAPsaTtPl32ClrxCK72wBkldcQ48GZkAAnUOaxttAtlJHuzwF5XjDiIBAAMCAAN5AAM2BA',
    '8Б': 'AgACAgIAAxkBAAPwaTtPlyTX4PBLJfkocKxF3pi-JcMAAnMOaxttAtlJ9ZqjWFdIgcIBAAMCAAN5AAM2BA',
    '8В': 'AgACAgIAAxkBAAPuaTtPl_yhCtr2ON_EItY_R2ES3ccAAnEOaxttAtlJz9zHMTcFZAQBAAMCAAN5AAM2BA',
    '8Г МЭ': 'AgACAgIAAxkBAAPtaTtPl0J6Pq3A2ioJ0Rm-17AEGbgAAnIOaxttAtlJ8I-sWJj_Ex8BAAMCAAN5AAM2BA',
    '8Г ХБ': 'AgACAgIAAxkBAAPvaTtPl52xzhvJ2qGBBkTvUE317hYAAnQOaxttAtlJpICnC6ssJq8BAAMCAAN5AAM2BA',
    '9А ФМ': 'AgACAgIAAxkBAAP2aTtQmJH5R6BJruetoIa2i9Tg8jkAAoAOaxttAtlJ5slH2lnQf8ABAAMCAAN5AAM2BA',
    '9А ФХ': 'AgACAgIAAxkBAAP4aTtQmd4-uMIcDfBkqfO9XSh5qPkAAoIOaxttAtlJUm6gwlqJUoQBAAMCAAN5AAM2BA',
    '9Б' : 'AgACAgIAAxkBAAP5aTtQmZqMeYc0QBXg-slBh-k66s8AAoEOaxttAtlJHnV2_9SuOtcBAAMCAAN5AAM2BA',
    '9В МЭ' : 'AgACAgIAAxkBAAP3aTtQmbLUDAmtcyFL4RMkUE6wytUAAn8OaxttAtlJLWWsv8E_JSIBAAMCAAN5AAM2BA',
    '9В ХБ' : 'AgACAgIAAxkBAAP6aTtQmQOAgaVYAuVJVGfqZC1y5I8AAoMOaxttAtlJ6aIVsHhOA1cBAAMCAAN5AAM2BA',
    '10А': 'AgACAgIAAxkBAAIBFGk7UbxuP_SfPxhunHrV6rCkPQmZAAKIDmsbbQLZSU6h2od79x7YAQADAgADeQADNgQ',
    '10Б': 'AgACAgIAAxkBAAIBFmk7Ubw_qKWTJXLAzSDAySuDfC8eAAKHDmsbbQLZSTAUoiJSeZGzAQADAgADeQADNgQ',
    '10В МЭ': 'AgACAgIAAxkBAAIBGGk7Ubwzv4tJ_rWUl2mU_sO3UrqJAAKGDmsbbQLZSae5Ech-SNiJAQADAgADeQADNgQ',
    '10В ХБ' : 'AgACAgIAAxkBAAIBFWk7Ubxoq-7rjDozJkFfk9qt7x3hAAKFDmsbbQLZSSbsLx6YdN33AQADAgADeQADNgQ',
    '11А':'AgACAgIAAxkBAAIBF2k7Ubw42a9W4BBJnVYcNFaZmANPAAKJDmsbbQLZSa2G08BdnjTfAQADAgADeQADNgQ',
    '11Б МИ':'AgACAgIAAxkBAAIBHmk7U2Uhr7qBJCGjdNY_2XgpFyjbAAKYDmsbbQLZSVcnXbFT1w5qAQADAgADeQADNgQ',
    '11Б ХБ': 'AgACAgIAAxkBAAIBH2k7U2Wx9xPay1MEYcN_fUtsHwJHAAKWDmsbbQLZSfTKJT4UrDZxAQADAgADeQADNgQ',
    '11Б ФХ': 'AgACAgIAAxkBAAIBIGk7U2U-7_IIAAF6SeStWVmfjWOXGwAClw5rG20C2Ul-8oyXodxF3gEAAwIAA3kAAzYE',
    '11В': 'AgACAgIAAxkBAAIBImk7U2XJ3StxbQLRgiK5s5JIER8wAAKZDmsbbQLZSW90aGEdhQraAQADAgADeQADNgQ',
    '11Г': 'AgACAgIAAxkBAAIBIWk7U2U5_OfdwwvPMMH4caBNNK-ZAAKaDmsbbQLZSW8Z0yx5BbP9AQADAgADeQADNgQ'
}

teachers = {
'администрация': ['Топешкин Дмитрий Александрович','Светлова Елена Михайловна' ,'Клоков Денис Юрьевич','Купров Павел Сергеевич'],
'история':['Назаров Роман Львович','Фомин Сергей Александрович','Адактуева Ольга Эдуардовна'],
'обществознание': ['Назаров Роман Львович','Фомин Сергей Александрович','Адактуева Ольга Эдуардовна'],
'математика': ['Светлова Елена Михайловна', 'Генералова Ирина Вячеславовна','Будилова Светлана Владимировна',
    'Заикин Евгений Юрьевич ','Сухова Дарья Александровна','Дарькина Галина Николаевна','Бардыкина Луиза Владимировна',
    'Кострикина Александра Игоревна','Иньков Владислав Леонидович', 'Зверева Наталья Леонидовна', 'Будилова Оксана Витальевна'],
'английский язык':['Безбородова Светлана Александровна','Исаева Юлия Владимировна',
                   'Кармалито Елизавета Евгеньевна','Поварешкина Александра Максимовна','Яким Наталья Леонидовна'],
'информатика': ['Будилов Виталий Аркадьевич', 'Будилова Оксана Витальевна'],
'география':['Амамбаева Алёна Маратовна'],
'русский язык':['Цветкова Наталия Львовна','Ляпина Евгения Олеговна','Андреева Светлана Юрьевна','Антошкина Наталья Владимировна'],
'литература': ['Цветкова Наталия Львовна','Ляпина Евгения Олеговна','Андреева Светлана Юрьевна','Антошкина Наталья Владимировна'],
'физра':['Литвиненко Валерий Павлович','Чуканов Роман Александрович'],
'биология':['Водовозова Светлана Александровна','Гариянц Наталья Михайловна'],
'физика':['Топешкин Дмитрий Александрович','Кирсанкина Алина Павловна','Лебедев Матвей Андреевич'],
'химия':['Скоринова Елена Александровна','Клоков Денис Юрьевич']}

lessons = [
(time(9, 00), time(9, 40)),
    (time(9, 55), time(10, 35)),
    (time(10, 50), time(11, 30)),
    (time(11, 40), time(12, 20)),
    (time(12, 40), time(13, 20)),
    (time(13, 40), time(14, 20)),
    (time(14, 40), time(15,20)),
    (time(15, 40), time(16, 10))
]

# кнопки
teacher_keyboard = [
    ["Расписание любого класса"],
    ["Расписание звонков - таймер урока"],
    ["Коллеги по предмету"],
    ['Новости школы', 'Обратная связь'],
    ['<< назад']
]
student_key = [
    ['Мое расписание'],
    ['Учителя школы'],
    ['Расписание звонков - таймер урока'],
    ['Расписание другого класса'],
    ['Изменить класс','Новости школы', 'Обратная связь'],
    ['<< назад']
]
parant_key = [
    ['Расписание ребенка'],
    ['Расписание звонков - когда перемена'],
    ['Учителя школы'],
    ['Изменить класс','Новости школы', 'Обратная связь'],
    ['<< назад']
]
async def get_photo_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file_id = photo.file_id
    await update.message.reply_text(f"file_id этой картинки:\n{file_id}")

#функция двойного выбора класса(4 раза будет использоваться)
async def safe_clas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # выбираем цифру класса
    context.user_data['show_teacher'] = False
    keyboard_numbers = [[num] for num in classi.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard_numbers, resize_keyboard=True)

    await update.message.reply_text(
        "Выберите класс:",
        reply_markup=reply_markup
    )

    # сохраняем состояние — что теперь ждём цифру класса
    context.user_data["waiting_for_grade_number"] = True

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # очищаем всё
    context.user_data.clear()

    keyboard = [["Ученик", "Учитель"], ["Родитель"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text("Выберите, кто вы:", reply_markup=reply_markup)

async def get_lesson_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    weekday = now.weekday()
    if weekday >= 5:
        await update.message.reply_text("Сегодня выходной! Уроков нет 🤗")
        return
    else:
        now_t = now.time()
        for i,(start,end) in enumerate(lessons, start=1):
            if start <= now_t <= end:
                minutes_left = int((datetime.combine(now.date(), end) -
                                    datetime.combine(now.date(), now_t)).seconds / 60)
                end_3p = datetime.combine(now.date(), time(14, 20))
                minuts_3p = int((end_3p - datetime.combine(now.date(), now_t)).total_seconds() / 60)

                end_4p = datetime.combine(now.date(), time(16, 10))
                minuts_4p = int((end_4p - datetime.combine(now.date(), now_t)).total_seconds() / 60)
                if now_t <(time(14, 20)):
                    await update.message.reply_text(
                    f"Сейчас {i}-й урок.\nДо конца урока осталось {minutes_left} мин.\nДо конца третьей пары {minuts_3p // 60} часов, {minuts_3p % 60}мин\nДо конца четвертой пары {minuts_4p//60} часов, {minuts_4p%60} мин."
                )
                elif now_t <= (time(16, 10)) and now_t >= (time(14, 20)):
                    await update.message.reply_text(f'Сейчас {i}-й урок.\nДо конца урока осталось {minutes_left} мин.\nДо конца третьей пары {minuts_3p// 60} часов, {minuts_3p% 60} мин.')
                return

        await update.message.reply_text("Сейчас внеурочное время. Пора отдохнуть!")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == 'Ученик':
        context.user_data['role'] = 'student'
        await safe_clas(update, context)
        return
    if text == 'Родитель':
        context.user_data['role'] = 'parant'
        await safe_clas(update, context)
        return
    if text == 'Учитель':
        context.user_data['role'] = 'teacher'
        reply_markup = ReplyKeyboardMarkup(teacher_keyboard, resize_keyboard=True)
        await update.message.reply_text(
            "Хорошо, вы учитель. Выберите, что вам нужно:",
            reply_markup=reply_markup)
        return

    if text == "Новости школы":
        await update.message.reply_text(
            "Новости школы можно посмотреть в нашем официальном канале:\n"
            "https://t.me/szaosch58"
        )
        return

    if text == '<< назад':
        if context.user_data.get("feedback_mode"):
            context.user_data["feedback_mode"] = False
        await back(update, context)
        return
    #обратная связь
    if text == "Обратная связь":
        await update.message.reply_text("Напишите сюда ваше предложение или замечание. Мы передим его администратору")
        context.user_data["feedback_mode"] = True
        return

    if text == 'Расписание звонков - таймер урока' or text == 'Расписание звонков - когда перемена':
        await get_lesson_status(update, context)
        return

    if text == 'Учителя школы':
        await update.message.reply_text('Напишите предмет, по которому хотите посмотреть список учителей в формате: Математика')
        context.user_data['show_teacher'] = True
        return

    if text == 'Коллеги по предмету':
        await update.message.reply_text('Напишите предмет, который вы преподаете в формате: Математика ,\nа мы выведем вам ваших коллег по предмету')
        context.user_data['show_teacher'] = True
        return

    if text == "Расписание любого класса" and context.user_data.get("role") == "teacher":
        context.user_data["wants_schedule"] = True
        await safe_clas(update, context)
        return
    if text == "Расписание другого класса" and context.user_data.get("role") == "student":
        context.user_data["wants_schedule"] = True
        await safe_clas(update, context)
        return
    if (text == 'Мое расписание' and context.user_data.get("role") == "student") or (text == 'Расписание ребенка' and context.user_data.get("role") == 'parant'):
        full_class = context.user_data.get("full_class")
        if not full_class:
            context.user_data["wants_HISschedule"] = True
            await update.message.reply_text("Сначала выберите ваш класс.")
            await safe_clas(update, context)
            return
        if full_class in schedule:
            await update.message.reply_photo(schedule[full_class])
        else:
            await update.message.reply_text("Пока нет расписания для вашего класса")
        return
    if text == "Изменить класс" and context.user_data.get("role") in ["student", "parant"]:
        context.user_data["change_class"] = True
        # удаляем ранее сохранённый класс
        context.user_data.pop("full_class", None)

        await safe_clas(update, context)
        return
    # пересылаем админу
    if context.user_data.get("feedback_mode"):
        admin_id = 1290443690
        await context.bot.send_message(
            chat_id=admin_id,
            text=f"📩 Новое сообщение от {update.effective_user.full_name} (@{update.effective_user.username}):\n\n{text}"
        )
        await update.message.reply_text("Спасибо! Ваше сообщение отправлено админу 😊")

        context.user_data["feedback_mode"] = False
        return
    if context.user_data.get('show_teacher'):
        subject = text.lower().strip()

        if subject in teachers:
            context.user_data['show_teacher'] = False
            teacher_list = "\n".join(teachers[subject])
            await update.message.reply_text(f'Учителя по предмету "{subject.capitalize()}" : \n{teacher_list}')
        else:
            await update.message.reply_text('Такого предмета нету, попробуйте ввести еще раз:')
        return


    # ждём выбор цифры класса
    if context.user_data.get("waiting_for_grade_number"):
        if text in classi:  # проверяем, что цифра существует
            context.user_data["grade_number"] = text    # сохраняем цифру

            # выбор буквы
            letters = classi[text]
            keyboard_letters = [[l] for l in letters]
            reply_markup = ReplyKeyboardMarkup(keyboard_letters, resize_keyboard=True)

            await update.message.reply_text('и букву',
                reply_markup=reply_markup
            )

            # переключаем состояние
            context.user_data["waiting_for_grade_number"] = False
            context.user_data["waiting_for_grade_letter"] = True
        else:
            await update.message.reply_text("Такого класса нет. Выберите цифру ещё раз.")


    # ждём выбор буквы класса
    elif context.user_data.get("waiting_for_grade_letter"):
        grade = context.user_data["grade_number"]

        if text not in classi[grade]:
            await update.message.reply_text("Такой буквы нет. Выберите букву ещё раз.")
            return
        if text in classi[grade]:
            context.user_data["grade_letter"] = text

            # сброс состояний
            context.user_data["waiting_for_grade_letter"] = False
            full_class = f"{grade}{text}"
            context.user_data["full_class"] = full_class

        if context.user_data.get("change_class"):
            context.user_data["change_class"] = False

            if context.user_data["role"] == "student":
                reply_markup = ReplyKeyboardMarkup(student_key, resize_keyboard=True)
                await update.message.reply_text(
                    f"Класс успешно изменён! Теперь вы ученик {full_class}.\nВыберите действие:",
                    reply_markup=reply_markup
                )
                return

            if context.user_data["role"] == "parant":
                reply_markup = ReplyKeyboardMarkup(parant_key, resize_keyboard=True)
                await update.message.reply_text(
                    f"Класс успешно изменён! Ваш ребёнок теперь в {full_class}.\nВыберите действие:",
                    reply_markup=reply_markup
                )
                return

        if context.user_data.get("wants_schedule"):
            # снимаем флаг
            context.user_data["wants_schedule"] = False

            #выводим картинку расписания
            if full_class in schedule:
                file_id = schedule[full_class]
                await update.message.reply_photo(file_id)
            else:
                await update.message.reply_text("Для этого класса пока нет расписания.")

            if context.user_data["role"] == "teacher":
                reply_markup = ReplyKeyboardMarkup(teacher_keyboard, resize_keyboard=True)

            else:
                reply_markup = ReplyKeyboardMarkup(student_key, resize_keyboard=True)
            await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)
            return
        if context.user_data.get("wants_HISschedule"):
            context.user_data["wants_HISschedule"] = False
            if full_class in schedule:
                await update.message.reply_photo(schedule[full_class])
            else:
                await update.message.reply_text("Пока нет расписания для вашего класса")


            if context.user_data["role"] == "teacher":
                reply_markup = ReplyKeyboardMarkup(teacher_keyboard, resize_keyboard=True)

            else:
                reply_markup = ReplyKeyboardMarkup(student_key, resize_keyboard=True)
            await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)
            return
        if context.user_data['role'] == 'student':
            reply_markup = ReplyKeyboardMarkup(student_key, resize_keyboard=True)
            await update.message.reply_text(
            f'Хорошо, вы ученик {full_class} класса, выберите, что вам нужно',
            reply_markup=reply_markup)
            return

        if context.user_data['role'] == 'parant':
            reply_markup = ReplyKeyboardMarkup(parant_key, resize_keyboard=True)
            await update.message.reply_text(
            f'Хорошо, ваш ребенок в {full_class} классе, выберите, что вам нужно',
            reply_markup=reply_markup)
            return
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"В этом боте вы сможете получить полезную информацию о расписании, звонках, коллегах и учителях")

    keyboard = [
        ["Ученик", "Учитель"],
        ["Родитель"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        f'Выберите кто вы:',
    reply_markup=reply_markup
    )
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start))
    app.add_handler(MessageHandler(filters.TEXT, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, get_photo_id))
    app.run_polling()


if __name__ == "__main__":
    main()

