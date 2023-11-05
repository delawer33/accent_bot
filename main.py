import telebot
import random
from telebot import types

from word_read import words
from variants import variants
bot = telebot.TeleBot('6725749795:AAHiHm-jWFeUNNWZKkgSDf6mCeXn0PsjAcc')

@bot.message_handler(commands=['start'])
def start(message):
    show_word(message)

words_to_repeat = []

def show_word(message):
    global words_to_repeat
    print(words_to_repeat)
    if len(words_to_repeat) != 0:
        if random.randint(1,3) == 1:
            right_ans = words_to_repeat[0]
            word = right_ans.lower()
            words_to_repeat.pop(0)
        else: 
            right_ans = random.choice(words)
            word = right_ans.lower()
    else:
        right_ans = random.choice(words)
        word = right_ans.lower()
    variants_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    variants_markup.add(*variants(word))
    mu_rep = bot.send_message(message.from_user.id, word, reply_markup=variants_markup)
    bot.register_next_step_handler(mu_rep, check_answer, right_ans)

def check_answer(answer, right_answer):
    global words_to_repeat
    if answer.text == right_answer:
        bot.send_message(answer.from_user.id, 'Верно✅')
    else:
        bot.send_message(answer.from_user.id, 'Ошибка❌, правильный ответ: {}'.format(right_answer))
        words_to_repeat.append(right_answer)
    show_word(answer)       

bot.polling(none_stop=True, interval=0)