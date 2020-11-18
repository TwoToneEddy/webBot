#!/usr/bin/python3
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from playsound import playsound

alert = './alert.wav'
vendor = './johnlewis.mp3'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")


LOGIN_MAIL = "lee.hudson1384@gmail.com"
LOGIN_PASSWORD = "HqdFJsE3SFyfM9n"
PS5_URL = "https://www.johnlewis.com/sony-playstation-5-console-with-dualsense-controller/white/p5115192"
ITEM_URL2 = "https://www.johnlewis.com/sony-playstation-5-dualsense-wireless-controller-white/p5192093"



driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
driver.get('https://auth.johnlewis.com/login?state=g6Fo2SBrbnRyalFaLXJ3SzZ3M0JlcDg1S1BuU3JkRWtyN0tyM6N0aWTZIEZaZFRvRzI2UUg4bTE4clpSajd5Nnp3STRuT194VHhFo2NpZNkgNlI2SWo3cGwwYzQyMzJReWZncGFQcnVoSHd1c0JqS1A&client=6R6Ij7pl0c4232QyfgpaPruhHwusBjKP&protocol=oauth2&prompt=login&response_type=code&redirect_uri=https%3A%2F%2Faccount.johnlewis.com%2Fauth0%2Fcallback&scope=openid%20profile%20email&audience=https%3A%2F%2Fapi.johnlewis.com&initialScreen=login&continue_url=https%3A%2F%2Fwww.google.com%2F')
time.sleep(5)
try:
    driver.find_element_by_xpath('//*[@id="pecr-cookie-banner-wrapper"]/div/div[1]/div/div[2]/button[1]').click()
except:
    pass

driver.find_element_by_id('email').send_keys(LOGIN_MAIL)
driver.find_element_by_id('password').send_keys(LOGIN_PASSWORD)
driver.find_element_by_id('loginForm').click()
time.sleep(5)
driver.get(PS5_URL) 
found = False
while(found == False):
    time.sleep(2.5)
    driver.refresh()
    try:
        a = driver.find_element_by_id('button--add-to-basket')
        playsound(alert)
        playsound(vendor)
        print("found!!!!!!!!!!!!!")
        found = True
        while(found ==  True):
            playsound(alert)
            playsound(vendor)
    except:
        pass
