import telebot
from config import TOKEN
from telebot import types

token = TOKEN
bot = telebot.TeleBot(token)

schedule = {
    "Понедельник": [
        "Создание ботов 12:00-13:30",
        "Программирование Сайта 15:00-16:30",
        "Обучение ИИ 18:00-19:30"
    ],
    "Среда": [
        "Создание ботов 10:00-11:30",
        "Программирование Сайта 13:00-14:30",
        "Обучение ИИ 16:00-17:30"
    ],
    "Пятница": [
        "Создание ботов 14:00-15:30",
        "Программирование Сайта 17:00-18:30",
        "Обучение ИИ 20:00-21:30"
    ],
}

admin_password = "65mary65"
is_admin = False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Информация", "Расписание", "Связь", "Вход в админ панель")
    bot.send_message(message.chat.id, 'Привет, ты попал в бота по онлайн-школе, выбери опцию ниже:', reply_markup=markup)

@bot.message_handler(regexp='Вход в админ панель')
def admin_login(message):
    bot.send_message(message.chat.id, 'Введите пароль для доступа к админ панель:')
    bot.register_next_step_handler(message, check_password)

def check_password(message):
    global is_admin
    if message.text == admin_password:
        is_admin = True
        bot.send_message(message.chat.id, 'Вы вошли в админ-панель. Чтобы изменить расписание, используйте команды "Редактировать(день)" и "Сохранить расписание".')
    else:
        bot.send_message(message.chat.id, 'Неверный пароль.')

@bot.message_handler(func=lambda message: is_admin and message.text.startswith('Редактировать'))
def edit_schedule(message):
    day = message.text.split(' ')[1]
    if day in schedule:
        bot.send_message(message.chat.id, f"Текущее расписание на {day}:\n" + "\n".join(schedule[day]) + "\nВведите новое расписание через запятую:")
        bot.register_next_step_handler(message, update_schedule, day)
    else:
        bot.send_message(message.chat.id, 'Такого дня не существует.')

def update_schedule(message, day):
    new_schedule = message.text.split(',')
    schedule[day] = [item.strip() for item in new_schedule]
    bot.send_message(message.chat.id, 'Расписание изменено!')

@bot.message_handler(func=lambda message: message.text == "Сохранить расписание" and is_admin)
def save_schedule(message):
    bot.send_message(message.chat.id, 'Расписание сохранено!')

@bot.message_handler(regexp='Связь')
def contact_info(message):
    bot.send_message(message.chat.id, 'Тех. Поддержка: @DenDona')

@bot.message_handler(regexp='Информация')
def info(message):
    bot.send_message(message.chat.id, 'Бот для онлайн-школы\nБот предоставляет данные об расписании уроков\nЕсли возникла проблема, обратитесь в тех. поддержку.')

@bot.message_handler(func=lambda message: message.text == "Расписание")
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Понедельник", "Среда", "Пятница", "Обратно")
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Обратно")
def go_back(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Информация", "Расписание", "Связь", "Вход в админ панель")
    bot.send_message(message.chat.id, 'Выбери опцию ниже:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Понедельник")
def monday(message):
    bot.send_message(message.chat.id, '• Понедельник\n' + '\n'.join(schedule["Понедельник"]))

@bot.message_handler(func=lambda message: message.text == "Среда")
def wednesday(message):
    bot.send_message(message.chat.id, '• Среда\n' + '\n'.join(schedule["Среда"]))

@bot.message_handler(func=lambda message: message.text == "Пятница")
def friday(message):
    bot.send_message(message.chat.id, '• Пятница\n' + '\n'.join(schedule["Пятница"]))

print("Запущен!")
bot.infinity_polling()
