from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

'''
Заходим на сайт
Нажимаем кнопку
Вешаем ожиданием на появление алерта в 3 секунды
При получении - нажимаем нужную кнопку
'''

def test_alert():
    driver = webdriver.Chrome()
    driver.get('http://testautomationpractice.blogspot.com/')
    driver.find_element_by_css_selector('div.widget-content button').click()
    try:
        WebDriverWait(driver,5).until(EC.alert_is_present(),'Timed out')
        alert = driver.switch_to.alert
        #alert.accept()
        alert.dismiss()
        print('alert accepted')
    except TimeoutException:
        print('no alert')
    sleep(2) # to check