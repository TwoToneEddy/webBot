#!/usr/bin/python3
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from playsound import playsound

alert = './alert.wav'
vendor = './amazon.mp3'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")


LOGIN_MAIL = "lee.hudson1384@yahoo.co.uk"
LOGIN_PASSWORD = "oxford"
PS5_URL = "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_3?dchild=1&keywords=ps5&qid=1605712146&sr=8-3"
ITEM_URL2 = "https://www.amazon.co.uk/PlayStation-5-DualSense-Wireless-Controller-Black/dp/B08H99BPJN/ref=sr_1_1?dchild=1&keywords=ps5&qid=1605717901&sr=8-1"



driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
driver.get('https://www.amazon.co.uk/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.uk%2Flog%2Fs%3Fk%3Dlog%2Bin%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=gbflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
driver.find_element_by_id('ap_email').send_keys(LOGIN_MAIL)
driver.find_element_by_id('continue').click()
driver.find_element_by_id('ap_password').send_keys(LOGIN_PASSWORD)
driver.find_element_by_id('signInSubmit').click()
time.sleep(15)
driver.get(PS5_URL) 
found = False
while(found == False):
    #print("Refreshing")
    driver.refresh()
    #driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[28]/div[1]/div/form/div[2]/ul/li[1]/span/div/span/span/span/button/div/div[1]/span').click()
    #print("Clicking")
    
    time.sleep(5)
    #print("Checking")
    try:
        a = driver.find_element_by_id('add-to-cart-button')
        playsound(alert)
        playsound(vendor)
        print("found!!!!!!!!!!!!!")
        found = True
        while(found ==  True):
            playsound(alert)
            playsound(vendor)
    except:
        pass
