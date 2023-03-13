from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from urllib import request
import datetime
import locale
import math
import random as rand

cats=[100,101,102,103,200,201,202,203,204,206,207,300,301,302,303,304,305,307,308,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,420,421,422,423,424,425,426,429,431,444,450,451,497,498,499,500,501,502,503,504,506,507,508,509,510,511,521,522,523,525,599]
months = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
cats_len = len(cats)

def binom(update: Update, context: CallbackContext) -> None:
    s = update.message.text
    l = len(s)
    integ = []
    p=0
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            p +=1
            integ.append(int(s_int))
    if p!=2:
        update.message.reply_text("Неверный ввод: Должно быть 2 элемента!!!")
    else:
        update.message.reply_text(f'Binom{integ[0], integ[1]}  = {math.comb(integ[0], integ[1])}')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Привет, {update.effective_user.first_name}')

def time(update: Update, context: CallbackContext) -> None:
    time_now = datetime.datetime.now()
    update.message.reply_text(f'Сейчас {time_now.hour}:{time_now.minute}, {time_now.day} {months[time_now.month-1]} {time_now.year} года')

def cat(update: Update, context: CallbackContext) -> None:
    cat_num = cats[rand.randint(0, cats_len-1)]
    url = 'https://http.cat/'+str(cat_num)
    response = request.urlopen(url)
    body = response.read()
    update.message.reply_photo(body)


with open('token') as token:
    updater = Updater(token.read().strip())

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('binom', binom))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('time', time))
updater.dispatcher.add_handler(CommandHandler('cat', cat))

updater.start_polling()
updater.idle()