from selenium import webdriver

'''
Создание скриншота двумя разными способами.
'''

def test_screen():
    driver = webdriver.Chrome()
    driver.get("http://goha.ru")
    driver.save_screenshot('screen.png')
    driver.get_screenshot_as_file('screen 2.png')