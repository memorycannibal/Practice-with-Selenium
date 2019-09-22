from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

'''
Заходим на сайт
Переключаемся во фрейм по его имени
Нажимаем на ссылку по тексту
Выходим из фрейма на базовый html
Переключаемся во фрейм по его имени
Нажимаем на ссылку по тексту
Выходим из фрейма на базовый html
'''
'''
Если на странице 1 фрейм или не важна поддержка кода,то можно использовать для перехода в него:
driver.switch_to.frame(0)
'''

def test_frame():
    driver = webdriver.Chrome()
    driver.get('https://seleniumhq.github.io/selenium/docs/api/java/')

    driver.switch_to.frame('packageListFrame')
    driver.find_element(By.LINK_TEXT,'org.openqa.selenium.html5').click()

    driver.switch_to.default_content()

    driver.switch_to.frame('packageFrame')
    driver.find_element(By.LINK_TEXT,'LocationContext').click()

    driver.switch_to.default_content()
    sleep(2) # to check