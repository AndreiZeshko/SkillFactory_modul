import telebot
from config import keys, TOKEN
from extensions import ConvertionException, Converter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text='Чтобы перевести валюту введите: \n<имя валюты>\n<в какую перевести>' \
         '\n<количество переводимой валюты>' \
         '\nЧтобы увидкть доступные валюты введите команду /values' \
         '\n p.s. Из за изменения API сайта переводить можно тольео <евро> в другую валюту.'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text= 'Доступные ваоюты:'
    for key in keys.keys():
        text ='\n'.join((text,key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    values = list(map(str.lower, values))
    try:
        if len(values) != 3:
            raise ConvertionException('Не верное количество параметров!')
        quote, base, amount = values
        total_base = Converter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)