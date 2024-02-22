import telebot
from telebot import types
import os

bot = telebot.TeleBot('6878290029:AAEaNCWUnrfHF1rXNshqBf9J8zN7OMmiHZE')

user_id=None
database=open('Base_File.txt','r+')
mess='None'
today=0

@bot.message_handler(commands=['start'])
def start(message):
    global user_id
    user_id = message.from_user.id
    global database
    database = open(str(user_id) + '.txt', 'x' and 'r+')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('НАЧАТЬ')
    btn2 = types.KeyboardButton('описание')
    btn3 = types.KeyboardButton('перезапуск')
    btn4 = types.KeyboardButton('меню')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Здарова, {message.from_user.first_name}',reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text==('описание'):
        bot.send_message(message.chat.id, 'Этот бот нужен, чтобы...', reply_markup=menu(message))
    elif message.text==('перезапуск'):
        bot.send_message(message.chat.id, '...готово', reply_markup=start(message))
    elif message.text==('меню'):
        bot.send_message(message.chat.id, f'Ваше меню, Сир {message.from_user.first_name}', reply_markup=menu(message))
    elif message.text==('НАЧАТЬ'):
        bot.send_message(message.chat.id, 'ещё в разработке', reply_markup=nach(message))
    elif message.text==('Повторения на сегодня'):
        bot.send_message(message.chat.id, '...загрузка повторений...', reply_markup=repeater(message))
    elif message.text==('Добавить сегодняшние темы'):
        bot.send_message(message.chat.id, '...подготовка к добавлению...', reply_markup=newtopic(message))

def menu(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('НАЧАТЬ')
    btn2 = types.KeyboardButton('описание')
    btn3 = types.KeyboardButton('перезапуск')
    btn4 = types.KeyboardButton('меню')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(btn4)
    bot.send_message(message.chat.id, '...menu',reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def nach(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Повторения на сегодня')
    btn2 = types.KeyboardButton('Добавить сегодняшние темы')
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, 'выберите действие',reply_markup=markup)
    bot.register_next_step_handler(message, on_click)




def repeater(message):
    global user_id
    global database

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Вывести')
    markup.row(btn1)


    day = 0

    g = database.readlines()
    d = {}

    for i in g:
        k = 0
        for s in i:
            k = k + 1
            if s == "|":
                break
        day = i[:k - 1]
        tema = i[k:-1]
        d[day] = tema

    today = int(day) + 1
    bot.send_message(message.chat.id, "сегодня " +str(today)+ " день обучения",reply_markup=markup)
    rep = []
    if today >= 121:
        rep1 = str(today - 120)
        rep.append(d[rep1])
    if today >= 8:
        rep2 = str(today - 7)
        rep.append(d[rep2])
    if today >= 6:
        rep3 = str(today - 5)
        rep.append(d[rep3])
    if today >= 2:
        rep4 = str(today - 1)
        rep.append(d[rep4])
    else:
        rep.append("нет")


    bot.send_message(message.chat.id, "темы для повторения:",reply_markup=markup)
    for o in rep:
        bot.send_message(message.chat.id, o)


    bot.register_next_step_handler(message, menu)


def newtopic(message):
    global mess
    mess = message.text.strip()
    global user_id
    global database

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Начать ввод')
    markup.row(btn1)

    day = 0

    g = database.readlines()

    for i in g:
        k = 0
        for s in i:
            k = k + 1
            if s == "|":
                break
        day = i[:k - 1]

    today = int(day) + 1
    today = str(today)

    bot.send_message(message.chat.id, "сегодня " + today + " день обучения",reply_markup=markup)
    bot.send_message(message.chat.id, "сегодняшняя новая тема ( ↓ Введите Ниже ↓ )",reply_markup=markup)
    database.write(today + "|" + mess + "\n")
    bot.register_next_step_handler(message, menu)







bot.infinity_polling()