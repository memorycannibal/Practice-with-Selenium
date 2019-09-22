import pickle
import time  
from selenium import webdriver
from time import sleep
from pytest import mark

# Сохранение/загрузка через профиль
'''
Работа с куками через профиль.
1й запуск - создаёт дерикторию с прифилем и всеми настройками внутри
2й запуск - использует всё что было сохранено  ранее
Тоже самое, что профиль, которым пользуемся мы на домашнем копьютере
'''
@mark.skip
def test_withUserData():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir=selenium") 
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://temp-mail.org/')
    time.sleep(3)

# Сохранение через pickle
'''
Работа с куками через пакет pickle ( сохранение ).
Создаём файл и в цикле запихиваем все наши куки из браузера.
Сохраняем файл.
'''
def test_exportCookie():  
    browser = webdriver.Chrome()
    browser.get('https://temp-mail.org/')
    with open('cookie.pkl','wb') as f:
        pickle.dump( browser.get_cookies(), f)

#Добавление через pickle
'''
Работа с куками через пакет pickle ( загрузка ).
Читаем созданный ранее файл с куками и в цикле засовываем их в браузер.
Перезагружаем страницу, чтобы сервер подхватил наши куки
'''
def test_importCookie():
    browser = webdriver.Chrome()
    browser.get('https://temp-mail.org/')
    browser.delete_all_cookies()
    with open('cookie.pkl','rb') as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            browser.add_cookie(cookie)
    browser.refresh()
    time.sleep(100)

