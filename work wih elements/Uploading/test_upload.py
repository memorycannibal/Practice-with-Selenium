from selenium import webdriver
from time import sleep

'''
Загрузка файла осуществляется путём указания пути до файла
'''

def test_upload():
    driver = webdriver.Chrome()
    driver.get('http://testautomationpractice.blogspot.com/')
    driver.switch_to.frame(0)
    driver.find_element_by_id('RESULT_FileUpload-11').send_keys('C://TestDownloadFolder/info.txt')
    sleep(3)