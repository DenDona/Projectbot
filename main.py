import telebot
from config import TOKEN
from telebot import types

token = TOKEN
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Информация", "Расписание", "Связь")
    bot.send_message(message.chat.id, 'Привет, ты попал в бота по онлайн-школе, выбери опцию ниже:', reply_markup=markup)



@bot.message_handler(regexp='Связь')
def contact_info(message):
    bot.send_message(message.chat.id, 'Тех. Поддержка: @DenDona')



@bot.message_handler(regexp='Информация')
def info(message):
    bot.send_message(message.chat.id, 'Бот для онлайн-школы\nБот предоставляет данные об расписание уроков\nЕсли напши проблему обратитесь по Связь-Написать подержке')



@bot.message_handler(func=lambda message: message.text == "Расписание")
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Понедельник", "Среда", "Пятница", "Обратно")
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text == "Обратно")
def go_back(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Информация", "Расписание", "Связь")
    bot.send_message(message.chat.id, 'Выбери опцию ниже:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Понедельник")
def monday(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, '• Понедельник\n• Создание ботов 12:00-13:30\n• Программировние Сайта 15:00-16:30\n• Обучение ИИ 18:00-19:30')



@bot.message_handler(func=lambda message: message.text == "Среда")
def wednesday(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, '• Среда\n• Создание ботов 10:00-11:30\n• Программировние Сайта 13:00-14:30\n• Обучение ИИ 16:00-17:30')


@bot.message_handler(func=lambda message: message.text == "Пятница")
def friday(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, '• Пятница\n• Создание ботов 14:00-15:30\n• Программировние Сайта 17:00-18:30\n• Обучение ИИ 20:00-21:30')



print("Запущен!")
bot.infinity_polling()