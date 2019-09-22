from selenium import webdriver

'''
Для получения числа рядов - 
Находим колличество тегов "tr" внутри таблицы
Для получения числа коллонок - 
Получаем колличество тегов "th" внутри первого тега "tr" <-- th это заголовки таблицы

for r in range(2,rows+1)
начинаем с 2, т.к 1й ряд - содержит только заголовки заголовки
rows+1,т.к цикл идёт до "значения -1"
'''


def test_table():
    driver = webdriver.Chrome()
    driver.get('https://www.w3schools.com/html/html_tables.asp')
    rows = len(driver.find_elements_by_css_selector('#customers tbody tr'))
    collumns = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th')) # th заголовки
    print('rows: {}, collumns {}'.format(rows,collumns))
    print('       Company                 Contract       Country')
    for r in range(2,rows+1): # со второго ряда, т.к первый заголовки
        for c in range(1,collumns+1):
            val = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[{}]/td[{}]'.format(r,c))
            print(val.text,end='           ')
        print()
