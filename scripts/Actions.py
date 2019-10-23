from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Actions():
    def __init__(self):
        pass

    def get_username(self, browser):
        username = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'nZSzR']/h1"))).text
        return username

    def get_profile(self, browser, profile):
        browser.get("https://www.instagram.com/" + profile)

    def get_postcount(self, browser):
        post_count = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li/span/span"))).text

    def get_post_url(self, browser, row, col):
        url = browser.find_element_by_xpath("//div[contains(@class, 'Nnq7C weEfm')]["+str(row)+"]/div["+str(col)+"]/a")
        return url.get_attribute("href")

    def like_picture(self, browser):
        try:
            like = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Like']")))
            like.click()
        except TimeoutException:
            pass

    def dislike_picture(self, browser):
        try:
            Unlike = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Unlike']")))
            like.click()
        except TimeoutException:
            pass

    def follow_user(self, browser):
        try:
            follow = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Follow')]")))
            follow.click()
        except TimeoutException:
            pass

    def unfollow_user(self, browser):
        try:
            following = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Following')]")))
            following.click()

            unfollow = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Unfollow')]")))
            unfollow.click()
        except TimeoutException:
            pass
