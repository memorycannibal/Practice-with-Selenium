from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

'''
Создаём пользовательские настройки.
Данные настройки указывают:
1. Куда скачиваем
2. Вывод уведомления о скачке
3. ?
4. Проверка ресурка из базы блэк листа на скам и т.п
'''
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {
  "download.default_directory": r"C:\TestDownloadFolder",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True 
})


def test_download_chrome():
    
    driver = webdriver.Chrome(options=chromeOptions)
    driver.maximize_window()
    driver.get('http://demo.automationtesting.in/FileDownload.html')
    driver.find_element_by_id('textbox').send_keys('testing')
    driver.find_element_by_id('createTxt').click()
    driver.find_element_by_id('link-to-download').click()
    sleep(1)
    driver.find_element_by_id('pdfbox').send_keys('test')
    driver.find_element_by_id('createPdf').click()
    driver.find_element_by_id('pdf-link-to-download').click()
    sleep(3)