from Farming import Farming
from FileHandling import FileHandling
from Browser import Browser
from UserStats import UserStats
import getpass
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Profile(Farming, FileHandling, Browser, UserStats):
    def __init__(self):
        #Account credentials
        self.email    = None
        self.password = None

        #Browser options
        Browser.__init__(self)

        #Account infos
        UserStats.__init__(self)

        #Account followers/following
        self.follower_list  = []
        self.following_list = []
        self.non_followback = []

        #Lists of users collected
        self.likers_collected           = []
        self.likers_collected_clean     = []
        self.commenters_collected       = []
        self.commenters_collected_clean = []
        self.private_list               = []

        #Farming options
        Farming.__init__(self)

    def initialize_profile(self):
        choice = input("Load an already existing profile? [YES/NO]: ")
        if choice.lower()  == "yes":
            self.print_profile_folders()
            self.user_name = input("Which account do you want to use? ")

            self.load_account_credentials()
            self.load_browser_config()
            self.load_farming_options()
            self.load_followers_list()
            self.load_following_list()
            self.load_non_followback_list()
            self.load_private_list()

            if self.browser_name.lower() == "firefox":
                self.create_browser_firefox()
            elif self.browser_name.lower() == "chrome":
                self.create_browser_chrome()

            self.login_instagram()

        elif choice.lower() == "no":
            self.email    = input("Enter email: ")
            self.password = getpass.getpass("Enter password: ")

            self.browser_name = input("Which browser do you want to use? [FIREFOX/CHROME]: ")
            if self.browser_name.lower() == "firefox":
                self.browser_name = "Firefox"
            elif self.browser_name.lower() == "Chrome":
                self.browser_name = "Chrome"

            self.proxy = input("Do you want to use a proxy? [YES/NO]: ")
            if self.proxy.lower() == "yes":
                self.proxy = input("Enter your proxy: ")
            else:
                self.proxy = None

            self.headless = input("Do you want the browser to be visible? [YES/NO]: ")
            if self.headless.lower() == "yes":
                self.headless = False
            else:
                self.headless = True

            self.user_agent = input("Do you want to use a custom user agent? [YES/NO]: ")
            if self.user_agent.lower() == "yes":
                self.user_agent = input("Enter your custom user agent: ")
            else:
                self.user_agent = None

            self.min_followers = input("Enter amount of followers the account should at least have: ")
            self.max_followers = input("Enter max amount of followers the account should have: ")
            self.min_following = input("Enter amount of following the account should at least have: ")
            self.max_following = input("Enter max amount of following the account should have: ")
            self.num_post      = input("How many posts the account should have: ")

            self.follow_user = input("Do you want to follow users? [YES/NO]: ")
            if self.follow_user.lower() == "yes":
                self.follow_user = True

                self.follow_per_day = input("How many do you want to follow every day: ")

                self.follow_if_private = input("Do you want to follow the account if it's empty? [YES/NO]: ")
                if self.follow_if_private.lower() == "yes":
                    self.follow_if_private = True
                else:
                    self.follow_if_private = False

                self.follow_if_empty = input("Do you want to follow the account if it's private? [YES/NO]: ")
                if self.follow_if_empty.lower() == "yes":
                    self.follow_if_empty = True
                else:
                    self.follow_if_empty = False

            else:
                self.follow_user       = False
                self.follow_if_private = False
                self.follow_if_empty   = False
                self.follow_per_day    = 0

            self.actions_per_hour = input("How many actions per hour do you feel safe performing: ")
            self.number_of_likes  = input("How many likes per profile do you want to leave: ")

            self.collect_commenters = input("Do you want to collects the commenters as well? [YES/NO]: ")
            if self.collect_commenters.lower() == "yes":
                self.collect_commenters = True
            else:
                self.collect_commenters = False

            if self.browser_name.lower() == "firefox":
                print("create firefox")
                self.create_browser_firefox()
            elif self.browser_name.lower() == "chrome":
                print("create chrome")
                self.create_browser_chrome()

            self.login_instagram()
            self.get_own_profile()

            self.user_name  = self.get_username()
            self.url        = self.current_url
            self.post_count = self.get_postcount()
            self.bio        = self.get_bio()
            self.follower   = self.get_followers_count()
            self.following  = self.get_following_count()

            self.create_profile_folder()
            self.write_account_credentials()
            self.write_browser_config()
            self.write_farming_options()
            self.load_followers_list()
            self.load_following_list()
            self.load_private_list()
            self.load_non_followback_list()

    def login_instagram(self):
        self.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

        time.sleep(random.randrange(1,4))

        login_box = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'username']")))
        self.realistic_typing(login_box, self.email)

        pwd_box = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'password']")))
        self.realistic_typing(pwd_box, self.password)

        login_button = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@type = 'submit']")))
        login_button.click()

        self.notifications_popup()
