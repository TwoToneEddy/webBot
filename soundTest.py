#!/usr/bin/python3
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from playsound import playsound

alert = './alert.wav'
vendor = './johnlewis.mp3'

playsound(alert)
playsound(vendor)

