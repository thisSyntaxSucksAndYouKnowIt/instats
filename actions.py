from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from realism import *

def remove_char(string, char):
    return re.sub(char,"", string)

def to_int(string):
    return int(string)

def login_insta(browser, email, password):
    login_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'username']")))
    realistic_typing(login_box, email)

    pwd_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'password']")))
    realistic_typing(pwd_box, password)

    login_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@type = 'submit']")))
    login_button.click()
    #//input[@name = 'username']
    #//input[@name = 'password']
    #//button[@type = 'submit']

def notifications_popup():
    popup_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
    popup_box.click()
    #//button[contains(text(), 'Turn On')]
    #//button[contains(text(), 'Not Now')]

def go_to_profile():
    #//span[@aria-label = 'Profile']
    pass

def get_username():
    #//div[@class = 'nZSzR']/h1
    pass

def get_postcount():
    #//li[@class = 'Y8-fY'][1]/a/span
    pass

def get_followers():
    #//li[@class = 'Y8-fY'][2]/a/span
    pass

def get_following():
    #//li[@class = 'Y8-fY'][3]/a/span
    pass

def is_empty():
    #//div[@class = 'v1Nh3 kIKUG _bz0w']
    pass

def like_picture():
    #//span[@aria-label = 'Like']
    pass

def dislike_picture():
    #//span[@aria-label = 'Unlike']
    pass

def comment_post():
    #//textarea[@aria-label = 'Add a comment…']
    #//button[@type = 'submit']
    pass
