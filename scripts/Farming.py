from Actions import Actions
from Realism import Realism
from UserStats import UserStats
from selenium.webdriver.common.action_chains import ActionChains

class Farming(Actions, Realism):
    def __init__(self):
        super().__init__()

    def collect_followers(self):
        prev_num = 1

        followers_button = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][2]")))
        followers_button.click()

        followers_popup = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'isgrP')]")))

        time.sleep(2)

        a = self.execute_script("return arguments[0].scrollTop;", followers_popup)
        b = self.execute_script("return arguments[0].scrollHeight;", followers_popup)
        c = self.execute_script("return arguments[0].clientHeight;", followers_popup)

        self.execute_script("arguments[0].scroll(0, 300);", followers_popup)
        time.sleep(2)

        while a/(b-c) != 1.0:
            self.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", followers_popup)
            number_available = len(self.find_elements_by_xpath("//li[@class = 'wo9IH']"))

            for i in range(prev_num, number_available):
                profile = self.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href")
                if profile not in self.followers_collected:
                    self.followers_list.append(profile)

            a = self.execute_script("return arguments[0].scrollTop;", followers_popup)
            b = self.execute_script("return arguments[0].scrollHeight;", followers_popup)
            c = self.execute_script("return arguments[0].clientHeight;", followers_popup)

            prev_num = number_available

    def collect_following(self):
        prev_num = 1

        following_button = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][3]")))
        following_button.click()

        following_popup = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'isgrP')]")))

        time.sleep(2)

        a = self.execute_script("return arguments[0].scrollTop;", following_popup)
        b = self.execute_script("return arguments[0].scrollHeight;", following_popup)
        c = self.execute_script("return arguments[0].clientHeight;", following_popup)

        self.execute_script("arguments[0].scroll(0, 300);", following_popup)
        time.sleep(2)

        while a/(b-c) != 1.0:
            self.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", following_popup)
            number_available = len(self.find_elements_by_xpath("//li[@class = 'wo9IH']"))

            for i in range(prev_num, number_available):
                profile = self.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href")
                if profile not in self.following_list:
                    self.following_list.append(profile)

            a = self.execute_script("return arguments[0].scrollTop;", following_popup)
            b = self.execute_script("return arguments[0].scrollHeight;", following_popup)
            c = self.execute_script("return arguments[0].clientHeight;", following_popup)

            prev_num = number_available

    def collect_commenters(self, profile_url):
        if profile_url != None:
            self.get(profile_url)

        load_more = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@aria-label, 'Load more comments')]")))

        #//ul[contains(@class, 'Mr508')][1]/div/li/div/div/div/h3                   user
        #//ul[contains(@class, 'Mr508')][1]/div/li/div/span/button                  like user comment
        #//ul[contains(@class, 'Mr508')][1]/div/li/div/div/div[2]/div/div/button[2] reply to comment
        #//textarea[contains(@aria-label, 'Add a comment…')]                        comment box
        #//button[contains(@type, 'submit')]                                        submit
        #//ul[contains(@class, 'Mr508')][1]/li/ul/li                                view replies
        #//ul[contains(@class, 'Mr508')][1]/li/ul/div/li/div/div/div/h3             replies
        #//ul[contains(@class, 'Mr508')][1]/li/ul/div/li/div/span                   like reply

    def farm_likers(self):
        self.get(url)

        like = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Nm9Fw')]/button")))
        like.click()
        like_popup = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'height: 356px; overflow: hidden auto;')]")))

        time.sleep(2)

        a = self.execute_script("return arguments[0].scrollTop;", like_popup)
        b = self.execute_script("return arguments[0].scrollHeight;", like_popup)
        c = self.execute_script("return arguments[0].clientHeight;", like_popup)

        while a/(b-c) != 1.0:
            num = len(self.find_elements_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div"))
            for i in range(1, num):
                try:
                    tab_1 = self.current_window_handle
                    user  = self.find_element_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div["+str(num)+"]/div[2]/div[1]")

                    ActionChains(self).key_down(Keys.CONTROL).click(user).key_up(Keys.CONTROL).perform()
                    tab_2 = self.window_handles[1]

                    self.(switch_to.window(tab_2))

                    if self.is_spam_prevention() == True:
                        return 1
                    else:
                        for usr in self.private_list:
                            if usr.url == self.current_url:
                                break

                            elif self.get_postcount() == 0:
                                if self.follow_if_empty == True:
                                    if self.follower_count > self.follow_per_day:
                                        self.follow_user()
                                        self.follower_count += 1

                            elif self.is_private() == True:
                                private_user = UserStats()

                                private_user.user_name     = self.get_username()
                                private_user.url           = self.current_url
                                private_user.bio           = self.get_bio()
                                private_user.num_followers = self.get_followers_count()
                                private_user.num_following = self.get_following_count()
                                private_user.num_posts     = self.get_post_count()

                                self.private_list.append(private_user)

                                if self.follow_if_private == True:
                                    if self.follower_count > self.follow_per_day:
                                        self.follower_count += 1
                                        self.follow_user()
                            else:
                                usr_followers  = self.get_followers_count()
                                usr_following  = self.get_following_count()
                                usr_post_count = self.get_post_count()

                                if self.collect_commenters == True:
                                    collect_commenters()

                                if usr_followers > self.min_followers and usr_post_count < self.max_followers:
                                    if self.follow_user == True:
                                        if self.follower_count > self.follow_per_day:
                                            self.follower_count += 1
                                            self.follow_user()

                                    if self.number_of_likes > 0:
                                        self.like_posts(self.number_of_likes, usr_post_count, None)

                                self.close()
                                self.(switch_to.window(tab_1))

                except NoSuchElementException:
                    return 0

            self.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", like_popup)

            time.sleep(2)

            a = self.execute_script("return arguments[0].scrollTop;", like_popup)
            b = self.execute_script("return arguments[0].scrollHeight;", like_popup)
            c = self.execute_script("return arguments[0].clientHeight;", like_popup)


def like_posts(self, number_of_likes, number_of_posts, profile_url):
    first_post = self.find_elements_by_xpath("//div[contains(@class, 'Nnq7C weEfm')][1]/div[1]")
    first_post.click()

    if number_of_likes > number_of_posts:
        like_count = number_of_posts

    if profile_url != None:
        self.get(profile_url)

    for x in range(1, like_count):
        self.like_picture()
        try:
            next_post = self.find_elements_by_xpath("//a[contains(@class, 'coreSpriteRightPaginationArrow')]")
            next_post.click()
        except NoSuchElementException:
            pass
