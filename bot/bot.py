import telebot
import requests
import sys
import traceback
from telebot.types import Message
from bs4 import BeautifulSoup
from variables import TOKEN

bot = telebot.TeleBot(TOKEN)

def get_urban_meaning(word):
    r = requests.get('https://www.urbandictionary.com/define.php?term={}'.format(word))
    soup = BeautifulSoup(r.text, features="lxml")
    meaning = soup.find('div',{'class':'meaning'})
    example = soup.find('div',{'class':'example'})
    try_these = soup.find('div',{'class':'try-these'})
    result = ''
    if meaning is not None:
        result += 'Meaning:\n{}\n'.format(meaning.text)
    if example is not None:
        result += 'Example:\n{}'.format(example.text)
    if try_these is not None:
        result += 'Sorry, can\'t find it ^('
    return result
 
@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    urban_meaning = get_urban_meaning(message.text)
    bot.reply_to(message, urban_meaning)


try:
    bot.polling()
except Exception as e:
    type_, value_, traceback_ = sys.exc_info()
    ex = traceback.format_exception(type_, value_, traceback_)
    print(ex)
    print('=====================================')
