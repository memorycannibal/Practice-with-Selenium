from selenium import webdriver
from time import sleep
from pytest import mark

'''
Перемещение ползунка  через JS методом scrollBy(откуда,на сколько)
'''
@mark.skip
def test_scroll_scrollBy():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
    driver.execute_script("window.scrollBy(0,1000)","")
    sleep(2)

'''
Перемещение ползунка  через JS методом scrollIntoView.
Страница перелестнётся на тот момент, когда искомый элемент будет в самом вверху страницы
'''
@mark.skip
def test_scroll_scroll_IntoView():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
    russianflag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[49]/td[1]/img')
    driver.execute_script("arguments[0].scrollIntoView();",russianflag)
    sleep(2)

'''
Перемещение ползунка  через JS методом scrollBy(откуда,на сколько)
Перемещение ползунка будет до конца страницы. А именно - до конца блока body
'''
def test_scroll_till_end():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    sleep(2)