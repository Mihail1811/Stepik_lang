import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_language(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form button')
    assert button is not None, 'Кнопка не найдена'
