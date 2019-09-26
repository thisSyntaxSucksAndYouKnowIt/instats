from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from actions import *

def is_empty(browser):
    try:
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'v1Nh3')]")))
    except TimeoutException:
        return True
    return False

def is_float(string):
    var = remove_char(string, ',')
    return int(var)

def is_already_liked(browser):
    try:
        liked = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Unlike']")))
    except TimeoutException:
        return False
    return True

def is_spam_prevention(browser):
    try:
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//p[contains(string(), 'Please wait a few minutes before you try again.')]")))
    except TimeoutException:
        return False
    return True

def is_username_wrong(browser):
    try:
        WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//p[contains(string(), 'The username you entered')]")))
    except TimeoutException:
        return False
    return True

def is_password_wrong(browser):
    try:
        WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//p[contains(string(), 'Sorry, your password was incorrect')]")))
    except TimeoutException:
        return False
    return False

def is_already_in(path, profile):
    with open(path) as f:
        unavailable = f.readlines()

    for line in unavailable:
        if profile in line:
            return True
    return False
