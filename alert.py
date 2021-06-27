import requests
from bs4 import BeautifulSoup
from threading import Timer
import telebot
URL = "https://www.amazon.in/Rockerz-255-Pro-Technology-Resistance/dp/B082VS5H3Y/ref=sr_1_16?crid=6YV5W3Q3TW8F&dchild=1&keywords=bluthoothearphone&qid=1612370071&sprefix=blu%2Caps%2C298&sr=8-16"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'
}


API_TOKEN = '1710137552:AAFKwuj96c6U7rZJCfWg2s3HqfpFJ9JLjQk'
ID = -1001566112738


set_price = 1000


def initialInfo():
    print("hey .. welcome .. ")
    printBot(" Starting alert tracking")
    printBot(" Current Set Price - " + str(set_price))
    printBot(" Current Set URL - " + URL)


def alert_system(product, link):
    bot = telebot.TeleBot(API_TOKEN)
    message = " Product :: " + product + " ,Link :: " + link
    bot.send_message(chat_id=ID, text=message)


def printBot(message):
    bot = telebot.TeleBot(API_TOKEN)
    bot.send_message(chat_id=ID, text=message)


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    printBot(product_title)
    price = soup.find(id='priceblock_ourprice').get_text()
    # print(price)
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    if float(product_price) <= set_price:
        alert_system(product_title, URL)
        printBot('sent')
        return
    else:
        print('not sent')
    Timer(60, check_price).start()


def driverFunction():
  initialInfo()
  check_price()


driverFunction()
