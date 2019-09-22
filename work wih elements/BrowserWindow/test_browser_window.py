from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

'''
    Переходим на сайт.
    Заполняем поле ввода
    Нажимаем кнопку
    Получаем список ссылок на Вики
    Открываем ссылку по тексту
    Получаем весь список окон(табов)
    Переключаемся между ними в цикле
    Если окно содержит "Boom" в title - закрываем его
    Переключаемся на оставшееся 
'''

def test_browser():
    driver = webdriver.Chrome()
    driver.get('http://testautomationpractice.blogspot.com/')
    driver.find_element_by_id('Wikipedia1_wikipedia-search-input').send_keys('Boom')
    driver.find_element_by_class_name('wikipedia-search-button').click()
    sleep(2)
    driver.find_element(By.LINK_TEXT,"Boom").click()

    handls = driver.window_handles
    for handle in handls:
        driver.switch_to.window(handle)
        print(driver.title)
        if 'Boom' in driver.title:
            driver.close() 
            driver.switch_to.window(handls[0]) 
            driver.find_element(By.LINK_TEXT,"Boom").click()
    sleep(2)