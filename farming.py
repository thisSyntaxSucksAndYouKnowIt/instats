from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from actions import *
import time
from tui import *

def collect_likers(browser, num_wanted, lists):
    lists.post_url = browser.current_url
    lists.user_name_post = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[1]/h2/a"))).text

    like = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Nm9Fw')]/button")))
    like.click()
    like_popup = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'height: 356px; overflow: hidden auto;')]")))

    time.sleep(2)

    a = browser.execute_script("return arguments[0].scrollTop;", like_popup)
    b = browser.execute_script("return arguments[0].scrollHeight;", like_popup)
    c = browser.execute_script("return arguments[0].clientHeight;", like_popup)

    while a/(b-c) != 1.0:
        num = len(browser.find_elements_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div"))
        for i in range(1, num):
            try:
                href = browser.find_element_by_xpath("//div[contains(@style, 'height: 356px; overflow: hidden auto;')]/div/div["+str(i)+"]/div[2]/div/div/a").get_attribute("href")
            except NoSuchElementException:
                return 0

            if href not in lists.likers_collected:
                lists.likers_collected.append(href)

                if len(lists.likers_collected) == num_wanted:
                    return lists

        clear_screen()
        title_screen()
        print("")
        print(" Collecting from user " + str(lists.user_name_post))
        print(" Collecting from posts: " + str(lists.post_url))
        print("")
        print(" Number of likers collected " + str(len(lists.likers_collected)))

        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", like_popup)

        time.sleep(2)

        a = browser.execute_script("return arguments[0].scrollTop;", like_popup)
        b = browser.execute_script("return arguments[0].scrollHeight;", like_popup)
        c = browser.execute_script("return arguments[0].clientHeight;", like_popup)

    return lists

def sort_profiles(browser, lists):
    usr_count = 1

    for usr in lists.likers_collected:
        browser.get(usr)

        clear_screen()
        title_screen()
        print(" Cleaning lists of user collected from " + str(lists.user_name_post))
        print(" Collected from posts: " + str(lists.post_url))
        print("")
        print(" Profile " + str(usr_count) + " out of " + str(len(lists.likers_collected)))
        print(" Clean profile collected: " + str(len(lists.likers_collected_clean)))

        if is_empty(browser) == False:
            lists.likers_collected_clean.append(usr)

        usr_count += 1

    return lists

def mass_like(browser, lists, number_of_likes):

    row = len(browser.find_elements_by_xpath("//div[contains(@class, 'Nnq7C weEfm')]"))
    profile_count = 1
    like_count = 0

    for usr in lists.likers_collected_clean:

        clear_screen()
        title_screen()
        print(" Profile " + str(profile_count) + " out of " + str(len(lists.likers_collected_clean)))
        print(" Like count: " + str(like_count))

        posts = []
        browser.get(usr)
        for r in (1, row):
            for c in (1, 3):
                if len(posts) == number_of_likes:
                    break
                else:
                    try:
                        posts.append(browser.find_element_by_xpath("//div[contains(@class, 'Nnq7C weEfm')]["+str(r)+"]/div["+str(c)+"]/a").get_attribute("href"))
                    except NoSuchElementException:
                        break

        for post in posts:
            print((len(posts)))
            browser.get(post)
            time.sleep(1)
            like_picture(browser)
            like_count += 1

        profile_count += 1

def collect_followers(browser, lists):

    lists.user_name_followers = get_username(browser)
    lists.user_url_followers = browser.current_url
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
        number_availabe = len(browser.find_elements_by_xpath("//li[@class = 'wo9IH']"))

        for i in range(prev_num, number_availabe):
            lists.followers_collected.append(browser.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href"))

        a = browser.execute_script("return arguments[0].scrollTop;", followers_popup)
        b = browser.execute_script("return arguments[0].scrollHeight;", followers_popup)
        c = browser.execute_script("return arguments[0].clientHeight;", followers_popup)

        prev_num = number_availabe

        clear_screen()
        title_screen()
        print(" Collecting followers from " + str(lists.user_name_followers))
        print("")
        print(" Number of followers collected: " + str(len(lists.followers_collected)))
        time.sleep(2)

    return lists

def collect_following(browser, lists):
    prev_num = 1

    lists.user_name_following = get_username(browser)
    lists.user_url_following = browser.current_url

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
        number_availabe = len(browser.find_elements_by_xpath("//li[@class = 'wo9IH']"))

        for i in range(prev_num, number_availabe):
            lists.following_collected.append(browser.find_element_by_xpath("//li[@class = 'wo9IH']["+str(i)+"]/div/div/div[2]/div/a").get_attribute("href"))

        a = browser.execute_script("return arguments[0].scrollTop;", following_popup)
        b = browser.execute_script("return arguments[0].scrollHeight;", following_popup)
        c = browser.execute_script("return arguments[0].clientHeight;", following_popup)

        prev_num = number_availabe

        clear_screen()
        title_screen()
        print(" Collecting following from " + str(lists.user_name_following))
        print("")
        print(" Number of following collected: " + str(len(lists.following_collected)))
        time.sleep(2)

    return lists

