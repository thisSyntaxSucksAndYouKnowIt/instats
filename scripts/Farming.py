from Actions import Actions

class Farming(Actions):
    def __init__(self):
        super().__init__()

    def collect_followers(self, browser):
        prev_num = 1

        followers_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][2]")))
        followers_button.click()

        followers_popup = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'isgrP')]")))

        time.sleep(2)

        a = browser.execute_script("return arguments[0].scrollTop;", followers_popup)
        b = browser.execute_script("return arguments[0].scrollHeight;", followers_popup)
        c = browser.execute_script("return arguments[0].clientHeight;", followers_popup)

        browser.execute_script("arguments[0].scroll(0, 300);", followers_popup)
        time.sleep(2)

        while a/(b-c) != 1.0:
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", followers_popup)
            number_available = len(browser.find_elements_by_xpath("//li[@class = 'wo9IH']"))

            for i in range(prev_num, number_available):
                profile = browser.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href")
                if profile not in self.followers_collected:
                    self.followers_list.append(profile)

            a = browser.execute_script("return arguments[0].scrollTop;", followers_popup)
            b = browser.execute_script("return arguments[0].scrollHeight;", followers_popup)
            c = browser.execute_script("return arguments[0].clientHeight;", followers_popup)

            prev_num = number_available

    def collect_following(self, browser):
        prev_num = 1

        following_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'Y8-fY')][3]")))
        following_button.click()

        following_popup = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'isgrP')]")))

        time.sleep(2)

        a = browser.execute_script("return arguments[0].scrollTop;", following_popup)
        b = browser.execute_script("return arguments[0].scrollHeight;", following_popup)
        c = browser.execute_script("return arguments[0].clientHeight;", following_popup)

        browser.execute_script("arguments[0].scroll(0, 300);", following_popup)
        time.sleep(2)

        while a/(b-c) != 1.0:
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", following_popup)
            number_available = len(browser.find_elements_by_xpath("//li[@class = 'wo9IH']"))

            for i in range(prev_num, number_available):
                profile = browser.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href")
                if profile not in self.following_list:
                    self.following_list.append(profile)

            a = browser.execute_script("return arguments[0].scrollTop;", following_popup)
            b = browser.execute_script("return arguments[0].scrollHeight;", following_popup)
            c = browser.execute_script("return arguments[0].clientHeight;", following_popup)

            prev_num = number_available

    def collect_commenters(self, browser):
        pass

    def farm_likers(self, browser):
        pass
