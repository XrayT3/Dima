# -*- coding: utf-8 -*-
import telebot
from telebot import types

token = "463092885:AAGhAgYvWqF0tjTKCa6m-0AsYpCsetSmYtQ"
welcome = "Введите свою историю.\nВ течении суток она будет прочитана модераторами и опубликована на канале."
admin_id = "211439710" #304123334

bot = telebot.TeleBot(token)


# Обработка /start команды - выдача клавиатуры
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, welcome)


@bot.message_handler(content_types=["text"])
def repeat(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Хотите ввести еще одну историю?']])
    bot.send_message(admin_id, '<b>Новое сообщение:</b>\n' + message.text + '\n\nАвтор письма:  @' +
                     message.from_user.username, parse_mode='HTML')
    bot.send_message(message.chat.id, 'Спасибо большое, Ваше сообщение отправлено.', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'Хотите ввести еще одну историю?':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                                  text='Напиши свою историю', parse_mode='HTML')


bot.polling(none_stop=True)
