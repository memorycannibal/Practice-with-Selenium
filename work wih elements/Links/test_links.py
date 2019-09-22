from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from pytest import mark

'''
Поиск ссылки по тегу
В примере: берется список всех ссылок, и нажимается случайна ссылка из этого списка
'''
@mark.skip
def test_links_tag_name():
    browser = webdriver.Chrome()
    browser.get('http://www.echoecho.com/htmlforms09.htm')
    links = browser.find_elements(By.TAG_NAME,"a")
    print ("Count of links on page :",len(links))
    rndnum =random.randint(0,len(links))
    print(links[rndnum].text)
    links[rndnum].click()


'''
Поиск ссылки по тексту
'''
@mark.skip
def test_links_link_text():
    browser = webdriver.Chrome()
    browser.get('http://www.echoecho.com/htmlforms09.htm')
    browser.find_element(By.LINK_TEXT,"HTML LINKS").click()

'''
Поиск ссылки по части теста ссылки. Выдаст туже ссылку, что и в прошлом примере
'''
def test_links_partial_link_text():
    browser = webdriver.Chrome()
    browser.get('http://www.echoecho.com/htmlforms09.htm')
    browser.find_element(By.PARTIAL_LINK_TEXT,"LINKS").click()