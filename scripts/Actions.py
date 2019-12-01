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
        username = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'nZSzR']/h1"))).text
        return username

    def get_profile(self, profile):
        self.get("https://www.instagram.com/" + profile)

    def get_own_profile(self):
        profile_icon = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'XrOey'][3]")))
        profile_icon.click()

    def get_postcount(self):
        post_count = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//li[1]/span/span"))).text
        return self.is_float(post_count)

    def get_bio(self):
        try:
            bio = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//section/div[2]/span"))).text
            return bio
        except TimeoutException:
            return "This user has no bio."

    def get_followers_count(self):
        follower_count = None
        try:
            follower_count = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][2]/span/span"))).text
        except TimeoutException:
            follower_count = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][2]/a/span"))).text

        return self.is_float(follower_count)

    def get_following_count(self):
        follower_count = None
        try:
            following_count = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][3]/span/span"))).text
        except TimeoutException:
            following_count = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][3]/a/span"))).text

        return self.is_float(following_count)

    def get_post_url(self, row, col):
        url = self.find_element_by_xpath("//div[contains(@class, 'Nnq7C weEfm')]["+str(row)+"]/div["+str(col)+"]/a")
        return url.get_attribute("href")

    def like_picture(self):
        try:
            like = WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Like']")))
            like.click()
        except TimeoutException:
            pass

    def dislike_picture(self):
        try:
            dislike = WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label = 'Unlike']")))
            dislike.click()
        except TimeoutException:
            pass

    def follow_user(self):
        try:
            follow = WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Follow')]")))
            follow.click()
        except TimeoutException:
            pass

    def unfollow_user(self):
        try:
            following = WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Following')]")))
            following.click()

            unfollow = WebDriverWait(self, 2).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Unfollow')]")))
            unfollow.click()
        except TimeoutException:
            pass

    def notifications_popup(self):
        popup_box = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        popup_box.click()

    def leave_comment(self, comment):
        comment_box   = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label = 'Add a comment…']")))
        self.realistic_typing(comment_box, comment)

        submit_button = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@type = 'submit']")))
        submit_button.click()
