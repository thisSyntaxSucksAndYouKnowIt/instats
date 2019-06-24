from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from actions import *
import time
from tui import *

def collect_likers(browser, num_wanted):
    usr_list = []

    #like = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Nm9Fw')]/a")))
    like = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "zV_Nj")))
    like.click()
    like_popup = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'height: 356px; overflow: hidden auto;')]")))

    time.sleep(2)

    a = browser.execute_script("return arguments[0].scrollTop;", like_popup)
    b = browser.execute_script("return arguments[0].scrollHeight;", like_popup)
    c = browser.execute_script("return arguments[0].clientHeight;", like_popup)

    while a/(b-c) != 1.0:
        num = len(browser.find_elements_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div"))
        for i in range(1, num):
            try:
                href = browser.find_element_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div["+str(i)+"]/div[2]/div/div/a").get_attribute("href")
            except NoSuchElementException:
                return 0

            if href not in usr_list:
                usr_list.append(href)

                if len(usr_list) == num_wanted:
                    return usr_list

        clear_screen()
        title_screen()
        print("Number of likers collected " + str(len(usr_list)))

        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", like_popup)

        time.sleep(2)

        a = browser.execute_script("return arguments[0].scrollTop;", like_popup)
        b = browser.execute_script("return arguments[0].scrollHeight;", like_popup)
        c = browser.execute_script("return arguments[0].clientHeight;", like_popup)

    return usr_list

def sort_profiles(browser, usr_list):
    clean_list = []

    usr_count = 1

    for usr in usr_list:
        browser.get(usr)

        clear_screen()
        title_screen()
        print("profile " + str(usr_count) + " out of " + str(len(usr_list)))
        print("clean profile collected: " + str(len(clean_list)))

        if is_empty(browser) == False:
            clean_list.append(usr)

        usr_count += 1

    return clean_list

def mass_like(browser, usr_list, number_of_likes):
    #//div[contains(@class, 'Nnq7C weEfm')][replace]/div[replace]/a

    row = len(browser.find_elements_by_xpath("//div[contains(@class, 'Nnq7C weEfm')]"))
    profile_count = 1
    like_count = 0

    for usr in usr_list:

        clear_screen()
        title_screen()
        print("Profile " + str(profile_count) + " out of " + str(len(usr_list)))
        print("Like count: " + str(like_count))

        posts = []
        browser.get(usr)
        for r in (1, row):
            for c in (1, 3):
                if len(posts) == number_of_likes:
                    break
                else:
                    try:
                        posts.append(browser.find_element_by_xpath("//div[contains(@class, 'Nnq7C weEfm')]["+str(r)+"]/div["+str(c)+"]/a").get_attribute("href"))
                    except NoSuchElementException:
                        break

        for post in posts:
            print((len(posts)))
            browser.get(post)
            time.sleep(1)
            like_picture(browser)
            like_count += 1

        profile_count += 1

def collect_followers(browser):
    #//li[@class = 'wo9IH'][num]/div/div/div[2]/div/a individual href
    #//li[@class = 'wo9IH'] number of href

    followers_list = []
    prev_num = 0

    followers_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][2]")))
    followers_button.click()

    followers_popup = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'PZuss')]")))

    time.sleep(2)

    a = browser.execute_script("return arguments[0].scrollTop;", like_popup)
    b = browser.execute_script("return arguments[0].scrollHeight;", like_popup)
    c = browser.execute_script("return arguments[0].clientHeight;", like_popup)


    while a/(b-c) != 1.0:
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", followers_popup)
        number_availabe = len(browser.find_elements_by_xpath("//li[@class = 'wo9IH']"))

        for i in range(prev_num, number_availabe):
            followers_list.append(browser.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href"))

        prev_num = number_availabe


    return followers_list

def collect_following(browser):
    pass
