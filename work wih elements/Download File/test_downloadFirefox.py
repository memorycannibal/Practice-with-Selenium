from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

'''
Создаём пользовательские настройки.
Данные настройки указывают:
1. Указываем что не надо выводить уведомление для файлов определенного типа
2. Убираем уведомление о загрузке
3. Указываем дерикторию для загрузки
4. ~Указываем что дериктория пользовательская
5. ~Убираем возможность открытия pdf в окне
'''
ffp = webdriver.FirefoxProfile()
ffp.set_preference('browser.helperApps.neverAsk.saveToDisk','text/plain,application/pdf') # Mime type
ffp.set_preference('browser.download.manager.showWhenStarting',False)
ffp.set_preference('browser.download.dir',r'C:\TestDownloadFolder') # C:\!   \ <--!
ffp.set_preference('browser.download.folderList',2)
ffp.set_preference('pdfjs.disabled',True)


def test_download_firefox():
    
    driver = webdriver.Firefox(firefox_profile=ffp)
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
    driver.quit()