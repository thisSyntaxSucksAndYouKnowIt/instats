from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions import *
import time

def collect_likers(browser, num_wanted):
    #//a[contains(@class, 'zV_Nj')]
    #//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div[number] individual posts
    #//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div[1]/div/div/a for href

    usr_list = []

    like = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'zV_Nj')]")))
    like.click()
    like_popup = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'height: 356px; overflow: hidden auto;')]")))

    time.sleep(2)

    a = browser.execute_script("return arguments[0].scrollTop;", like_popup)
    b = browser.execute_script("return arguments[0].scrollHeight;", like_popup)
    c = browser.execute_script("return arguments[0].clientHeight;", like_popup)

    while a/(b-c) != 1.0:
        num = len(browser.find_elements_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div"))
        for i in range(1, num):
            href = browser.find_element_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div["+str(i)+"]/div[2]/div/div/a").get_attribute("href")
            if href not in usr_list:
                usr_list.append(href)

                if len(usr_list) == num_wanted:
                    return usr_list

        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", like_popup)

        time.sleep(2)

        a = browser.execute_script("return arguments[0].scrollTop;", like_popup)
        b = browser.execute_script("return arguments[0].scrollHeight;", like_popup)
        c = browser.execute_script("return arguments[0].clientHeight;", like_popup)


    return usr_list

def sort_profiles(browser, usr_list):
    pass
