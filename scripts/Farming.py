from Actions import Actions
from UserStats import UserStats
from selenium.webdriver.common.action_chains import ActionChains

class Farming(Actions):
    def __init__(self):
        super().__init__()

    def collect_followers(self):
        prev_num = 1

        followers_button = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][2]")))
        followers_button.click()

        followers_popup = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'isgrP')]")))

        time.sleep(2)

        a = self.browser.execute_script("return arguments[0].scrollTop;", followers_popup)
        b = self.browser.execute_script("return arguments[0].scrollHeight;", followers_popup)
        c = self.browser.execute_script("return arguments[0].clientHeight;", followers_popup)

        self.browser.execute_script("arguments[0].scroll(0, 300);", followers_popup)
        time.sleep(2)

        while a/(b-c) != 1.0:
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", followers_popup)
            number_available = len(self.browser.find_elements_by_xpath("//li[@class = 'wo9IH']"))

            for i in range(prev_num, number_available):
                profile = self.browser.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href")
                if profile not in self.followers_collected:
                    self.followers_list.append(profile)

            a = self.browser.execute_script("return arguments[0].scrollTop;", followers_popup)
            b = self.browser.execute_script("return arguments[0].scrollHeight;", followers_popup)
            c = self.browser.execute_script("return arguments[0].clientHeight;", followers_popup)

            prev_num = number_available

    def collect_following(self):
        prev_num = 1

        following_button = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][3]")))
        following_button.click()

        following_popup = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'isgrP')]")))

        time.sleep(2)

        a = self.browser.execute_script("return arguments[0].scrollTop;", following_popup)
        b = self.browser.execute_script("return arguments[0].scrollHeight;", following_popup)
        c = self.browser.execute_script("return arguments[0].clientHeight;", following_popup)

        self.browser.execute_script("arguments[0].scroll(0, 300);", following_popup)
        time.sleep(2)

        while a/(b-c) != 1.0:
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", following_popup)
            number_available = len(self.browser.find_elements_by_xpath("//li[@class = 'wo9IH']"))

            for i in range(prev_num, number_available):
                profile = self.browser.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href")
                if profile not in self.following_list:
                    self.following_list.append(profile)

            a = self.browser.execute_script("return arguments[0].scrollTop;", following_popup)
            b = self.browser.execute_script("return arguments[0].scrollHeight;", following_popup)
            c = self.browser.execute_script("return arguments[0].clientHeight;", following_popup)

            prev_num = number_available

    def collect_commenters(self):
        pass

    def farm_likers(self):
        self.browser.get(url)

        like = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Nm9Fw')]/button")))
        like.click()
        like_popup = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'height: 356px; overflow: hidden auto;')]")))

        time.sleep(2)

        a = self.browser.execute_script("return arguments[0].scrollTop;", like_popup)
        b = self.browser.execute_script("return arguments[0].scrollHeight;", like_popup)
        c = self.browser.execute_script("return arguments[0].clientHeight;", like_popup)

        while a/(b-c) != 1.0:
            num = len(self.browser.find_elements_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div"))
            for i in range(1, num):
                try:
                    user = self.browser.find_element_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div["+str(num)+"]/div[2]/div[1]")

                except NoSuchElementException:
                    return 0

            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", like_popup)

            time.sleep(2)

            a = self.browser.execute_script("return arguments[0].scrollTop;", like_popup)
            b = self.browser.execute_script("return arguments[0].scrollHeight;", like_popup)
            c = self.browser.execute_script("return arguments[0].clientHeight;", like_popup)

            if self.is_spam_prevention() == True:
                return 1

            elif self.get_postcount() == 0:
                if self.follow_if_empty == True:
                   self.follow_user()

            elif self.is_private() == True:
                private_user = UserStats()

                private_user.user_name     = self.get_username()
                private_user.url           = self.browser.current_url
                private_user.bio           = self.get_bio()
                private_user.num_followers = self.get_followers_count()
                private_user.num_following = self.get_following_count()
                private_user.num_posts     = self.get_post_count()

                self.unavailable.append(private_user)

                if self.follow_if_private == True:
                    self.follow_user()
            else:
                usr_followers  = self.get_followers_count()
                usr_following  = self.get_following_count()
                usr_post_count = self.get_post_count()

                if usr_followers > self.min_followers and usr_post_count < self.max_followers:
                    pass
