from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import webbrowser


import os
import pyautogui





url = 'https://app.frupro.com'
gcp= "https://console.cloud.google.com/appengine?referrer=search&project=frupro-staging"
bitbucket="https://bitbucket.org/frupro/workspace/projects/FPBESERVICES"
clickup="https://app.clickup.com/2538736/v/l/f/90050082645?pr=66111669"
xero="https://go.xero.com/app/!V6Zc3/dashboard"
mongodb= "https://www.mongodb.com"

webbrowser.open(url, new=1)
webbrowser.open(gcp, new=1)
webbrowser.open(bitbucket, new=1)
webbrowser.open(clickup, new=1)
webbrowser.open(xero, new=1)
webbrowser.open(mongodb, new=1)


time.sleep(3)
pyautogui.click(x=1818,y=14)




pyautogui.click(x=1919,y=1057)
time.sleep(1)
pyautogui.hotkey('ctrl','alt', 't')
time.sleep(15)
# pyautogui.click(x=224,y=215)
pyautogui.click(x=267,y=164)
time.sleep(1)
pyautogui.click(x=814,y=971)
pyautogui.typewrite('Gunaydin herkese...')
pyautogui.click(x=987,y=966)
pyautogui.press('enter')



