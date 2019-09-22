from selenium import webdriver
from pytest import mark
from time import sleep

'''
Нажатие на радио боксы и чекбоксы аналогично нажатию на любой другой элемент.
is_selected() возвращает True/False в зависимости от нажат ли объект.
'''


def test_rb():
    browser = webdriver.Chrome()
    browser.get('http://www.echoecho.com/htmlforms10.htm')
    rb = browser.find_elements_by_css_selector('input[name="radio1"]')
    status = (rb[2].is_selected())
    print(status)
    rb[0].click()
    sleep(2)


def test_ch():
    browser = webdriver.Chrome()
    browser.get('http://www.echoecho.com/htmlforms09.htm')
    cb = browser.find_elements_by_css_selector('input[name="Checkbox"]')
    status = (cb[1].is_selected())
    print(status)
    cb[0].click()
    sleep(2)