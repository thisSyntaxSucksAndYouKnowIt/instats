from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Checks import Checks

class Actions(Checks):
    def __init__(self):
        pass

    def get_username(self):
        username = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'nZSzR']/h1"))).text
        return username

    def get_profile(self, profile):
        self.browser.get("https://www.instagram.com/" + profile)

    def get_postcount(self):
        post_count = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li/span/span"))).text
        return self.is_float(string)

    def get_post_url(self, row, col):
        url = self.browser.find_element_by_xpath("//div[contains(@class, 'Nnq7C weEfm')]["+str(row)+"]/div["+str(col)+"]/a")
        return url.get_attribute("href")

    def like_picture(self):
        try:
            like = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Like']")))
            like.click()
        except TimeoutException:
            pass

    def dislike_picture(self):
        try:
            dislike = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Unlike']")))
            dislike.click()
        except TimeoutException:
            pass

    def follow_user(self):
        try:
            follow = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Follow')]")))
            follow.click()
        except TimeoutException:
            pass

    def unfollow_user(self):
        try:
            following = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Following')]")))
            following.click()

            unfollow = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Unfollow')]")))
            unfollow.click()
        except TimeoutException:
            pass
