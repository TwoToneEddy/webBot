import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
driver.get('https://bank.barclays.co.uk/olb/authlogin/loginAppContainer.do#/identification')
time.sleep(1)

driver.find_element_by_id('label-sortCode-main').click()
driver.find_element_by_id('surname0').send_keys("Hudson")
driver.find_element_by_id('sortCode0').send_keys("20")
driver.find_element_by_id('sortCode1').send_keys("97")
driver.find_element_by_id('sortCode2').send_keys("48")
driver.find_element_by_id('sortCode3').send_keys("90443700")
driver.find_element_by_xpath('//*[@id="login-bootstrap"]/div/div[1]/div/div[1]/div[1]/div[1]/div[4]/section/form/div/div/div/div[11]/div/button').click()
time.sleep(5)

actions = ActionChains(driver) 
actions.send_keys(Keys.TAB * 7)
actions.perform()
actions = ActionChains(driver) 
actions.send_keys("o")
actions.perform()
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