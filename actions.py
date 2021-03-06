from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import os
from realism import *
from checks import *

def instats_init():
    try:
        os.makedirs("Instats/Config/")
    except FileExistsError:
        print(" Folder already exists")
        pass

    try:
        os.mknod("Instats/Config/config.txt")
    except FileExistsError:
        print(" Folder already exists")
        pass

    try:
        os.makedirs("Instats/Instats_Profiles")
    except FileExistsError:
        print(" Folder already exists")
        pass

    try:
        os.mknod("Instats/Instats_Profiles/unavailable.txt")
    except FileExistsError:
        print(" Unavailable file already exists")
        pass

def create_profile_folders(browser):
    try:
        os.makedirs("Instats/Instats_Profiles/" + str(get_username(browser)))
    except FileExistsError:
        print(" " + str(get_username(browser)) + " folder already exists")
        pass

    try:
        os.mknod("Instats/Instats_Profiles/" + str(get_username(browser) + "/followers.txt"))
    except FileExistsError:
        print(" Followers file already exists")
        pass

    try:
        os.mknod("Instats/Instats_Profiles/" + str(get_username(browser) + "/following.txt"))
    except FileExistsError:
        print(" Following file already exists")
        pass

    try:
        os.mknod("Instats/Instats_Profiles/" + str(get_username(browser) + "/followers_clean.txt"))
    except FileExistsError:
        print(" Followers clean file already exists")
        pass

    try:
        os.mknod("Instats/Instats_Profiles/" + str(get_username(browser) + "/following_clean.txt"))
    except FileExistsError:
        print(" Following clean file already exists")
        pass

    try:
        os.mknod("Instats/Instats_Profiles/" + str(get_username(browser) + "/non_followback.txt"))
    except FileExistsError:
        print(" Non followback file already exists")
        pass

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
    f = open(path, "a+")

    for profile in profile_list:
        if is_already_in(path, profile) == False:
            if '\n' in profile:
                f.write(profile)
            else:
                f.write(profile + '\n')
    f.close()

def load_file(path, lists, which_list, clean):
    f = open(path, "r")

    fill_list = None

    if which_list == 1:
        if clean == True:
            fill_list = lists.followers_collected_clean
            lists.user_name_followers = os.path.basename(os.path.dirname(path))
        else:
            fill_list = lists.followers_collected
            lists.user_name_followers = os.path.basename(os.path.dirname(path))
    elif which_list == 2:
        if clean == True:
            fill_list = lists.following_collected_clean
            lists.user_name_following = os.path.basename(os.path.dirname(path))
        else:
            fill_list = lists.following_collected
            lists.user_name_following = os.path.basename(os.path.dirname(path))
    elif which_list == 3:
        if clean == True:
            fill_list = lists.commenters_collected_clean
            lists.user_name_commenters = os.path.basename(os.path.dirname(path))
        else:
            fill_list = lists.commenters_collected
            lists.user_name_commenters = os.path.basename(os.path.dirname(path))

    for profile in f:
        if profile in fill_list:
            pass
        else:
            fill_list.append(profile)

    f.close()
    return lists

def list_profile_folders():
    folders = []
    path = "Instats/Instats_Profiles"
    dirs = os.listdir(path)

    for f in dirs:
        folders.append(f)

    folders = sorted(folders)
    return folders
