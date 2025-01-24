import os, sys
import telebot
from requests.exceptions import ConnectionError, ReadTimeout
from telebot import types
import time
from datetime import datetime

TOKEN = '...' #Здесь ваш токен из BotFather
bot = telebot.TeleBot(TOKEN)

needed_time = ''

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуй, боец! Давай настроим напоминания о твоей регулярной тренировке тела и духа!")
    clock(message)

def clock(message):
    body = types.InlineKeyboardMarkup(row_width = 1)
    item = types.InlineKeyboardButton('Силовые', callback_data='hi')
    item1 = types.InlineKeyboardButton('Статика', callback_data='hi1')
    item2 = types.InlineKeyboardButton('Динамика', callback_data='hi2')
    body.add(item, item1, item2)
    bot.send_message(message.chat.id, 'Выбери тип упражнений:', reply_markup = body)

@bot.callback_query_handler(func=lambda call:True)
def data(call):
    days = types.InlineKeyboardMarkup(row_width = 1)
    day1 = types.InlineKeyboardButton('Понедельник', callback_data='mon')
    day2 = types.InlineKeyboardButton('Вторник', callback_data='tue')
    day3 = types.InlineKeyboardButton('Среда', callback_data='wed')
    day4 = types.InlineKeyboardButton('Четверг', callback_data='thu')
    day5 = types.InlineKeyboardButton('Пятница', callback_data='fri')
    day6 = types.InlineKeyboardButton('Суббота', callback_data='sat')
    day7 = types.InlineKeyboardButton('Воскресенье', callback_data='sun')
    day_none = types.InlineKeyboardButton('Вернуться', callback_data='back')
    days.add(day1, day2, day3, day4, day5, day6, day7, day_none)
    if call.message:
        if call.data == 'hi':
            bot.send_message(call.message.chat.id, 'Выбери день недели:', reply_markup = days)
        elif call.data == 'hi1':
            bot.send_message(call.message.chat.id, 'Выбери день недели:', reply_markup = days)
        elif call.data == 'hi2':
            bot.send_message(call.message.chat.id, 'Выбери день недели:', reply_markup = days)
        elif call.data == 'back':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, clock(call.message))
        hour(call)
  
def hour(call):
    hours = types.InlineKeyboardMarkup(row_width = 2)
    hour1 = types.InlineKeyboardButton('12:00', callback_data='0')
    hour2 = types.InlineKeyboardButton('13:00', callback_data='1')
    hour3 = types.InlineKeyboardButton('14:00', callback_data='2')
    hour4 = types.InlineKeyboardButton('15:00', callback_data='3')
    hour5 = types.InlineKeyboardButton('16:00', callback_data='4')
    hour6 = types.InlineKeyboardButton('17:00', callback_data='5')
    hour7 = types.InlineKeyboardButton('18:00', callback_data='6')
    hour8 = types.InlineKeyboardButton('19:00', callback_data='7')
    hours.add(hour1, hour2, hour3, hour4, hour5, hour6, hour7, hour8)
    if call.message:
        if call.data == 'mon':
            bot.send_message(call.message.chat.id, 'Выбери подходящее время (со второй половины дня):', reply_markup = hours)
        elif call.data == 'tue':
            bot.send_message(call.message.chat.id, 'Выбери подходящее время (со второй половины дня):', reply_markup = hours)
        elif call.data == 'wed':
            bot.send_message(call.message.chat.id, 'Выбери подходящее время (со второй половины дня):', reply_markup = hours)
        elif call.data == 'thu':
            bot.send_message(call.message.chat.id, 'Выбери подходящее время (со второй половины дня):', reply_markup = hours)
        elif call.data == 'fri':
            bot.send_message(call.message.chat.id, 'Выбери подходящее время (со второй половины дня):', reply_markup = hours)
        elif call.data == 'sat':
            bot.send_message(call.message.chat.id, 'Выбери подходящее время (со второй половины дня):', reply_markup = hours)
        elif call.data == 'sun':
            bot.send_message(call.message.chat.id, 'Выбери подходящее время (со второй половины дня):', reply_markup = hours)
        nice(call)

def nice(call):
    
    if call.message:
        if call.data == '0':
            global needed_time
            needed_time = '12:00:00'
            bot.send_message(call.message.chat.id, 'Отлично! Напоминание установлено! Не пропусти тренировку, боец!\nЧтобы изменить время, введи /start')
            while needed_time == '12:00:00':
                t = time.ctime().split(' ')[3]
                if t == needed_time:
                    bot.send_message(call.message.chat.id, f"Напоминание о тренировке в {t} часов дня!", parse_mode="Markdown")
                    time.sleep(2)

        elif call.data == '1':
            needed_time = '13:00:00'
            bot.send_message(call.message.chat.id, 'Отлично! Напоминание установлено! Не пропусти тренировку, боец!\nЧтобы изменить время, введи /start')
            while needed_time == '13:00:00':
                t = time.ctime().split(' ')[3]
                if t == needed_time:
                    bot.send_message(call.message.chat.id, f"Напоминание о тренировке в {t} часов дня!", parse_mode="Markdown")
                    time.sleep(2)

        elif call.data == '2':
            needed_time = '14:00:00'
            bot.send_message(call.message.chat.id, 'Отлично! Напоминание установлено! Не пропусти тренировку, боец!\nЧтобы изменить время, введи /start')
            while needed_time == '14:00:00':
                t = time.ctime().split(' ')[3]
                if t == needed_time:
                    bot.send_message(call.message.chat.id, f"Напоминание о тренировке в {t} часов дня!", parse_mode="Markdown")
                    time.sleep(2)

        elif call.data == '3':
            needed_time = '15:00:00'
            bot.send_message(call.message.chat.id, 'Отлично! Напоминание установлено! Не пропусти тренировку, боец!\nЧтобы изменить время, введи /start')
            while needed_time == '15:00:00':
                t = time.ctime().split(' ')[3]
                if t == needed_time:
                    bot.send_message(call.message.chat.id, f"Напоминание о тренировке в {t} часов дня!", parse_mode="Markdown")
                    time.sleep(2)

        elif call.data == '4':
            needed_time = '16:00:00'
            bot.send_message(call.message.chat.id, 'Отлично! Напоминание установлено! Не пропусти тренировку, боец!\nЧтобы изменить время, введи /start')
            while needed_time == '16:00:00':
                t = time.ctime().split(' ')[3]
                if t == needed_time:
                    bot.send_message(call.message.chat.id, f"Напоминание о тренировке в {t} часов дня!", parse_mode="Markdown")
                    time.sleep(2)

        elif call.data == '5':
            needed_time = '17:00:00'
            bot.send_message(call.message.chat.id, 'Отлично! Напоминание установлено! Не пропусти тренировку, боец!\nЧтобы изменить время, введи /start')
            while needed_time == '17:00:00':
                t = time.ctime().split(' ')[3]
                if t == needed_time:
                    bot.send_message(call.message.chat.id, f"Напоминание о тренировке в {t} часов дня!", parse_mode="Markdown")
                    time.sleep(2)

        elif call.data == '6':
            needed_time = '18:00:00'
            bot.send_message(call.message.chat.id, 'Отлично! Напоминание установлено! Не пропусти тренировку, боец!\nЧтобы изменить время, введи /start')
            while needed_time == '18:00:00':
                t = time.ctime().split(' ')[3]
                if t == needed_time:
                    bot.send_message(call.message.chat.id, f"Напоминание о тренировке в {t} часов дня!", parse_mode="Markdown")
                    time.sleep(2)

        elif call.data == '7':
            needed_time = '19:00:00'
            bot.send_message(call.message.chat.id, 'Отлично! Напоминание установлено! Не пропусти тренировку, боец!\nЧтобы изменить время, введи /start')
            while needed_time == '19:00:00':
                t = time.ctime().split(' ')[3]
                if t == needed_time:
                    bot.send_message(call.message.chat.id, f"Напоминание о тренировке в {t} часов дня!", parse_mode="Markdown")
                    time.sleep(2)

try:
    bot.infinity_polling(timeout=10, long_polling_timeout = 5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
