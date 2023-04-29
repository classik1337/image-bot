from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import io
import requests
import time
import telebot
from telebot import types



bot = telebot.TeleBot('5823483810:AAHMH062KNxdSFKVCMPvYSxInKzzBNtrTVQ')

def dog(url,folder,file):
    driver = webdriver.Edge()
    driver.get(url=url)
    time.sleep(2)
    actions = ActionChains(driver)
    images = driver.find_elements(By.CLASS_NAME, "MMImage-Origin")
    time.sleep(2)
    NameImage = 'img.jpg'
    i = 0
    while i <= 2:
        for image in images:
            url = image.get_attribute("src")
            print("Image URL:", url)

            os.makedirs(file, exist_ok=True)  # CHANGE_______________
            img_bytes = requests.get(url).content
            img_binary = io.BytesIO(img_bytes)
            PathToImage = folder + str(i) + NameImage
            with open(PathToImage, 'wb') as f:
                f.write(img_binary.getvalue())
        time.sleep(1)  # Ожидание переключения картинки нахуй!!!
        actions.key_down(Keys.DOWN).perform()
        actions.key_up(Keys.DOWN).perform()
        i = i + 1


@bot.message_handler(commands=['start'])
def start(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Начать")
     markup.add(btn1)
     bot.send_message(message.from_user.id, "Нажми начать!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):


    if message.text == 'Начать':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
            btn1 = types.KeyboardButton('Dog')
            btn2 = types.KeyboardButton('Cat')
            btn3 = types.KeyboardButton('Capybara')
            btn4 = types.KeyboardButton('Rat')
            btn5 = types.KeyboardButton('Pig')
            btn6 = types.KeyboardButton('Monkey')
            markup.add(btn1, btn2,btn3,btn4,btn5,btn6)
            bot.send_message(message.from_user.id, '1 картинка = 1-2 секунды(их всего 3)!', reply_markup=markup)
    elif message.text == 'Dog':
        url =  'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi.pinimg.com%2Foriginals%2Ff5%2F0e%2Fa5%2Ff50ea536a1350024ea2e2de2fc3ccc40.jpg&lr=50&pos=0&rpt=simage&text=funny%20dog'
        folder = 'Dog/'
        file='Dog'
        dog(url,folder,file)
        z = 0
        while z <= 2:
            bot.send_photo(message.chat.id,
                           open('C:\\Users\\89125\\PycharmProjects\\PictDownload\\UpdateEdge\\Dog\\' + str(z) + 'img.jpg',
                                'rb'))
            z = z + 1
    elif message.text == 'Cat':
        url = 'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi.pinimg.com%2Foriginals%2Fed%2F8f%2Fde%2Fed8fde10bc1b0d506e20743708466d34.jpg&lr=50&pos=0&rpt=simage&text=funny%20cat'
        folder = 'Cat/'
        file = 'Cat'
        dog(url,folder,file)
        z = 0
        while z <= 2:
            bot.send_photo(message.chat.id,
                           open('C:\\Users\\89125\\PycharmProjects\\PictDownload\\UpdateEdge\\Cat\\' + str(
                               z) + 'img.jpg',
                                'rb'))
            z = z + 1
    elif message.text == 'Сapybara':
        url = 'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fmykaleidoscope.ru%2Fx%2Fuploads%2Fposts%2F2022-09%2F1663115129_18-mykaleidoscope-ru-p-zlaya-kapibara-krasivo-20.jpg&lr=50&pos=0&rpt=simage&text=%D1%81%D0%BC%D0%B5%D1%88%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%B0%D0%BF%D0%B8%D0%B1%D0%B0%D1%80%D1%8B'
        folder = 'Сapybara/'
        file = 'Сapybara'
        dog(url, folder, file)
        z = 0
        while z <= 2:
            bot.send_photo(message.chat.id,
                           open('C:\\Users\\89125\\PycharmProjects\\PictDownload\\UpdateEdge\\Сapybara\\' + str(
                               z) + 'img.jpg',
                                'rb'))
            z = z + 1
    elif message.text == 'Rat':
        url = 'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi.ytimg.com%2Fvi%2Fo_-bcd5WRfo%2Fmaxresdefault.jpg&lr=50&pos=0&rpt=simage&text=funny%20rat'
        folder = 'Rat/'
        file = 'Rat'
        dog(url, folder, file)
        z = 0
        while z <= 2:
            bot.send_photo(message.chat.id,
                           open('C:\\Users\\89125\\PycharmProjects\\PictDownload\\UpdateEdge\\Rat\\' + str(
                               z) + 'img.jpg',
                                'rb'))
            z = z + 1
    elif message.text == 'Pig':
        url = 'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fak.picdn.net%2Fshutterstock%2Fvideos%2F33329947%2Fthumb%2F1.jpg&lr=50&pos=0&rpt=simage&text=funny%20pig'
        folder = 'Pig/'
        file = 'Pig'
        dog(url, folder, file)
        z = 0
        while z <= 2:
            bot.send_photo(message.chat.id,
                           open('C:\\Users\\89125\\PycharmProjects\\PictDownload\\UpdateEdge\\Pig\\' + str(
                               z) + 'img.jpg',
                                'rb'))
            z = z + 1
    elif message.text == 'Monkey':
        url = 'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fwallpaper-mania.com%2Fwp-content%2Fuploads%2F2018%2F09%2FHigh_resolution_wallpaper_background_ID_77700037506.jpg&lr=50&pos=0&rpt=simage&text=funny%20monkey'
        folder = 'Monkey/'
        file = 'Monkey'
        dog(url, folder, file)
        z = 0
        while z <= 2:
            bot.send_photo(message.chat.id,
                           open('C:\\Users\\89125\\PycharmProjects\\PictDownload\\UpdateEdge\\Monkey\\' + str(
                               z) + 'img.jpg',
                                'rb'))
            z = z + 1
bot.polling(none_stop=True)











