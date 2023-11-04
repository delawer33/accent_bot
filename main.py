import telebot
import random
from telebot import types

from word_read import words
from variants import variants

bot = telebot.TeleBot('6725749795:AAHiHm-jWFeUNNWZKkgSDf6mCeXn0PsjAcc')

@bot.message_handler(commands=['start'])
def start(message):
    show_word(message)

def show_word(message):
    right_ans = random.choice(words)
    word = right_ans.lower()
    variants_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    variants_markup.add(*variants(word))
    mu_rep = bot.send_message(message.from_user.id, word, reply_markup=variants_markup)
    bot.register_next_step_handler(mu_rep, check_answer, right_ans)

def check_answer(answer, right_answer):
    if answer.text == right_answer:
        bot.send_message(answer.from_user.id, 'Верно✅')
    else:
        bot.send_message(answer.from_user.id, 'Ошибка❌, правильный ответ: {}'.format(right_answer))
    show_word(answer)       

bot.polling(none_stop=True, interval=0)