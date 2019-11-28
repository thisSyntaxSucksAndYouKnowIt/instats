from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re

class Checks:
    def __init__(self):
        pass

    def is_empty(self):
        try:
            WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'v1Nh3')]")))
        except TimeoutException:
            return True
        return False

    def is_private(self):
        try:
            WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(string(), 'This Account is Private')]")))
        except TimeoutException:
            return False
        return True

    def is_float(self, string):
        var = re.sub(',','', string)
        return int(var)

    def is_already_liked(self):
        try:
            liked = WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Unlike']")))
        except TimeoutException:
            return False
        return True

    def is_spam_prevention(self):
        try:
            WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//p[contains(string(), 'Please wait a few minutes before you try again.')]")))
        except TimeoutException:
            return False
        return True

    def is_username_wrong(self):
        try:
            WebDriverWait(self, 3).until(EC.presence_of_element_located((By.XPATH, "//p[contains(string(), 'The username you entered')]")))
        except TimeoutException:
            return False
        return True

    def is_password_wrong(self):
        try:
            WebDriverWait(self, 3).until(EC.presence_of_element_located((By.XPATH, "//p[contains(string(), 'Sorry, your password was incorrect')]")))
        except TimeoutException:
            return False
        return False
