from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions import *

def collect_likers(browser, num_wanted):
    #//a[contains(@class, 'zV_Nj')]
    #//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div[number] individual posts

    usr_list = []

    like = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'zV_Nj')]")))
    like.click()
    like_popup = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'height: 356px; overflow: hidden auto;')]")))

def sort_profiles(browser, usr_list):
    pass
