from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from pytest import mark

'''
Выбор нужного варианта из выпадающего меню тремя способами.
select_by_visible_text - по тексту
select_by_index - по индексу/порядку
select_by_value - по значению аттрибута value у нужного нам варианта
'''

@mark.skip
def test_select():
    browser = webdriver.Chrome()
    browser.get('http://htmlbook.ru/html/select')
    dropElement = Select(browser.find_element_by_css_selector('select[name="select2"]'))
    
    dropElement.select_by_visible_text('Чебурашка')
    sleep(2)

    dropElement.select_by_index(3)
    sleep(2)

    # by value
    #dropElement.select_by_value('value')

    browser.quit()


'''
объекс select имеет метод option - возращающий все доступные элементы
Пробегаемся по списку и выводим текст каждого
'''
def test_cout():
    #pytest -s
    browser = webdriver.Chrome()
    browser.get('http://htmlbook.ru/html/select')
    dropElement = Select(browser.find_element_by_css_selector('select[name="select2"]'))
    print(len(dropElement.options))
    allOption = dropElement.options
    for option in allOption:
        print(option.text)
    browser.quit()


    