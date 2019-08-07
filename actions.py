from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import os
from realism import *

def instats_init(browser):
    try:
        os.makedirs("Instats_Profiles")
    except FileExistsError:
        print("Folder already exists")
        pass

    choice = input("Press Enter to continue ...")

def create_profile_folders(browser):
    try:
        os.makedirs("Instats_Profiles/" + str(get_username(browser)))
    except FileExistsError:
        print("Own profile folder already exists")
        pass

    try:
        os.mknod("Instats_Profiles/" + str(get_username(browser) + "/followers.txt"))
    except FileExistsError:
        print("Followers file already exists")
        pass

    try:
        os.mknod("Instats_Profiles/" + str(get_username(browser) + "/following.txt"))
    except FileExistsError:
        print("Following file already exists")
        pass

def remove_char(string, char):
    return re.sub(char,'', string)

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
    username = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'nZSzR']/h1"))).text
    return username

def get_postcount(browser):
    #//li[@class = 'Y8-fY'][1]/a/span
    post_count = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')]/span/span"))).text
    return is_float(post_count)

def get_followers_count(browser):
    #//li[@class = 'Y8-fY'][2]/a/span
    follower_count = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][2]/a/span"))).get_attribute("title")
    return is_float(follower_count)

def get_following_count(browser):
    #//li[@class = 'Y8-fY'][3]/a/span
    following_count = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][3]/a/span"))).text
    return is_float(following_count)

def get_number_of_likers(browser):
    num_likers = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Nm9Fw')]/button/span"))).text
    return is_float(num_likers)

def is_float(string):
    var = remove_char(string, ',')
    return int(var)

def is_empty(browser):
    #//div[@class = 'v1Nh3 kIKUG _bz0w']
    try:
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'v1Nh3')]")))
    except TimeoutException:
        return True

    return False

def like_picture(browser):
    #//span[@aria-label = 'Like']
    try:
        like = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Like']")))
        like.click()
    except TimeoutException:
        pass

def dislike_picture(browser):
    #//span[@aria-label = 'Unlike']
    try:
        Unlike = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Unlike']")))
        like.click()
    except TimeoutException:
        pass

def comment_post():
    #//textarea[@aria-label = 'Add a comment…']
    #//button[@type = 'submit']
    pass

def write_file(path, profile_list):
    f = open(path, "w+")

    for profile in profile_list:
        f.write(profile)

    f.close()
