from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
from realism import *

def remove_char(string, char):
    return re.sub(char,'', string)

def to_int(string):
    var = remove_char(string, ',')
    return int(var)

def login_insta(browser, email, password):
    login_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'username']")))
    realistic_typing(login_box, email)

    pwd_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'password']")))
    realistic_typing(pwd_box, password)

    login_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@type = 'submit']")))
    login_button.click()

def notifications_popup(browser):
    popup_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
    popup_box.click()
    #//button[contains(text(), 'Turn On')]
    #//button[contains(text(), 'Not Now')]

def go_to_profile(browser):
    profile_icon = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Profile']")))
    profile_icon.click()

def get_username(browser):
    #//div[@class = 'nZSzR']/h1
    username = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'nZSzR']/h1"))).text()
    return username

def get_postcount(browser):
    #//li[@class = 'Y8-fY'][1]/a/span
    post_count = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')]/span/span"))).text
    return to_int(post_count)

def get_followers_count(browser):
    #//li[@class = 'Y8-fY'][2]/a/span
    follower_count = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][2]/a/span"))).get_attribute("title")
    return to_int(follower_count)

def get_following_count(browser):
    #//li[@class = 'Y8-fY'][3]/a/span
    following_count = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][3]/a/span"))).text
    return to_int(following_count)

def get_number_of_likers(browser):
    num_likers = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'zV_Nj')]/span"))).text
    return to_int(num_likers)

def is_empty(browser):
    #//div[@class = 'v1Nh3 kIKUG _bz0w']
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'v1Nh3 kIKUG _bz0w']")))
    except TimeoutException:
        return True
    return False

def like_picture():
    #//span[@aria-label = 'Like']
    like = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Like']")))
    like.click()

def dislike_picture():
    #//span[@aria-label = 'Unlike']
    Unlike = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Unlike']")))
    like.click()

def comment_post():
    #//textarea[@aria-label = 'Add a comment…']
    #//button[@type = 'submit']
    pass
