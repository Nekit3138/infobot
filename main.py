from lib import Api
import telebot

bot = telebot.TeleBot('1674625177:AAFyt68T5RjX0JTCCgjwyMEEgD2nFFX7cdM')
send = bot.send_message

start_text = '/weather для вывода погоды\n/rates для получения курсов валют'

after_weather = False

@bot.message_handler(content_types=['text'])
def new_command(message):
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row('/weather', '/rates')
    chat = message.chat.id
    text = message.text.lower()
    global after_weather
    if after_weather:
        try:
            res = Api.beauty_weather(text)
        except:
            
            send(chat, 'Неверный город', reply_markup=kb)
            after_weather = False
            return
        keys = ['Город', 'Температура', 'Ощущается', 'Давление', 'Влажность', 'Скорость ветра', 'Направление ветра',
                'Дождь', 'Снег', 'Облачность']
        vals = list(res.values())
        data = []
        for i in range(len(keys)):
            data.append(f'{keys[i]}:  {vals[i]}')
        send(chat, '\n'.join(data), reply_markup=kb)
        after_weather = False
    if text.startswith('/start'):
        send(chat, start_text, reply_markup=kb)
    elif text.startswith('/weather'):
        send(chat, 'Введите город')
        after_weather = True
    elif text.startswith('/rates'):
        res = list(Api.rate().values())
        data = []
        names = ['Доллар к рублю', 'Евро к рублю', 'Евро к доллару']
        for i in range(3):
            data.append(f'{names[i]}:  {res[i]}')
        kb = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        kb.row('/weather', '/rates')
        send(chat, '\n'.join(data), reply_markup=kb)


bot.polling()
