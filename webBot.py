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
LOGIN_PASSWORD = "7EV2MNpWdhbzAa5"
PS5_URL = "https://www.johnlewis.com/sony-playstation-5-console-with-dualsense-controller/white/p5115192"
ITEM_URL2 = "https://www.johnlewis.com/sony-playstation-5-dualsense-wireless-controller-white/p5192093"



driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
driver.get('https://www.currys.co.uk/gbuk/s/authentication.html')
time.sleep(5)
try:
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
except:
    pass
driver.find_element_by_id('input-sEmail').send_keys(LOGIN_MAIL)
driver.find_element_by_id('input-sPassword').send_keys(LOGIN_PASSWORD)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/form/div[3]/button').click()
time.sleep(5)
driver.get(PS5_URL) 

found = False
while(found == False):
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