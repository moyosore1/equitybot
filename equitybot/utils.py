import re
from datetime import datetime
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

import undetected_chromedriver as uc



def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument("--headless")
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = uc.Chrome(options=options)
    return driver


def convert_str_to_float(string):
    string.replace(" ", "")
    numeric_string = re.sub("[^.0-9]", "", string)
    return float(numeric_string)


def convert_str_to_time(string):
    string.replace(" ", "")
    time_string = re.sub("[^:0-9]", "", string)
    time_obj = datetime.strptime(time_string[1:], '%H:%M:%S').time()
    return time_obj


def login_to_mql5(driver):
    driver.get('https://trade.mql5.com/')
    time.sleep(3)
    login_element = driver.find_element(By.ID, "login")
    login_element.send_keys(66337396)
    password_element = driver.find_element(By.ID, "password")
    password_element.send_keys('lnja32')
    server_element = driver.find_element(By.ID, "server")
    server_element.clear()
    server_element.send_keys('ICMarketsSC-Demo06')

    okay_btn_xpath = "//button[contains(text(), 'OK')]"

    okay_btn = driver.find_element(By.XPATH, okay_btn_xpath)
    time.sleep(1)
    okay_btn.click()


def scrape_data(driver):
    market_watch_xpath = "/html/body/div[5]/div/div[1]"
    time.sleep(15)
    market_watch_element = driver.find_element(By.XPATH, market_watch_xpath)


    market_watch = convert_str_to_time(market_watch_element.text)

    balance_equity_xpath = "/html/body/div[6]/div[3]/table/tbody/tr[2]/td[1]/div/span"
    balance_equity_element = driver.find_element(
        By.XPATH, balance_equity_xpath)

    balance_equity_str = balance_equity_element.text
    balance_index = balance_equity_str.index("Balance:")
    equity_index = balance_equity_str.index("Equity:")
    margin_index = balance_equity_str.index("Margin")
    balance = convert_str_to_float(
        balance_equity_str[balance_index:equity_index].strip())
    equity = convert_str_to_float(
        balance_equity_str[equity_index:margin_index].strip())
    
    return market_watch, balance, equity
