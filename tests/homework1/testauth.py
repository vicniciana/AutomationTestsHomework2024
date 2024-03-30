import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def create_browser():
    #options = Options()
    #options.add_argument("--headless")
    #browser = webdriver.Chrome(options)
    browser = webdriver.Chrome()
    return browser

def test_auth_correct_data():
    browser = create_browser()
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html'
    browser.find_element(By.XPATH, '//*[@id="inventory_filter_container"]/div[contains(., "Products")]')
    # time.sleep(5)
    
    browser.close()

def test_auth_incorrect_data():
    browser = create_browser()
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/'
    browser.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3[@data-test="error"]')
    browser.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3[@data-test="error"]/button')
    browser.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3[@data-test="error" and contains(., "Epic sadface: ")]')
    #time.sleep(3)
    
    browser.close()



