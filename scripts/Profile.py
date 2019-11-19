from Farming import Farming
from FileHandling import FileHandling
from Browser import Browser
from UserStats import UserStats
import getpass

class Profile(Farming, FileHandling, Browser, UserStats):
    def __init__(self):
        #Account credentials
        self.email    = None
        self.password = None

        #Browser options
        self.browser_name = None
        self.proxy        = None
        self.headless     = None
        self.user_agent   = None
        self.browser      = None

        #Account infos
        self.user_name   = None
        self.profile_url = None
        self.post_count  = None
        self.bio         = None
        self.follower    = None
        self.following   = None

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
        self.min_followers      = None
        self.max_followers      = None
        self.min_following      = None
        self.max_following      = None
        self.num_post           = None
        self.follow_if_private  = None
        self.follow_if_empty    = None
        self.follow_user        = None
        self.follow_per_day     = None
        self.follow_count       = None
        self.actions_per_hour   = None
        self.number_of_likes    = None
        self.collect_commenters = None

    def initialize_profile(self):
        choice = input("Load an already existing profile? [YES/NO]: ")
        if choice.lower()  == "yes":
            self.user_name = input("Which account do you want to use? ")

            self.load_account_credentials()
            self.load_browser_config()
            self.load_farming_options()
            self.load_followers_list()
            self.load_following_list()
            self.load_non_followback_list()
            self.load_private_list()

            self.browser = Browser(self.browser_name, self.proxy, self.headless, self.user_agent)
            login_instagram()

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
                self.headless = True
            else:
                self.headless = False

            self.user_agent = input("Do you want to use a custom user agent? [YES/NO]: ")
            if self.user_agent.lower() == "yes":
                self.user_agent = input("Enter your custom user agent: ")
            else:
                self.user_agent = None

            self.min_followers      = input("Enter amount of followers the account should at least have: ")
            self.max_followers      = input("Enter max amount of followers the account should have: ")
            self.min_following      = input("Enter amount of following the account should at least have: ")
            self.max_following      = input("Enter max amount of following the account should have: ")
            self.num_post           = input("How many posts the account should have: ")

            self.follow_user        = input("Do you want to follow users? [YES/NO]: ")
                if self.follow_user.lower() == "yes":
                    self.follow_user = True
                else:
                    self.follow_user = False


            self.follow_if_private  = input("Do you want to follow the account if it's empty? [YES/NO]: ")
                if self.follow_if_private.lower() == "yes":
                    self.follow_if_private = True
                else:
                    self.follow_if_private = False

            self.follow_if_empty    = input("Do you want to follow the account if it's private? [YES/NO]: ")
                if self.follow_if_empty.lower() == "yes":
                    self.follow_if_empty = True
                else:
                    self.follow_if_empty = False


            self.follow_per_day     = input("How many do you want to follow every day: ")
            self.actions_per_hour   = input("How many actions per hour do you feel safe performing: ")
            self.number_of_likes    = input("How many likes per profile do you want to leave: ")

            self.collect_commenters = input("Do you want to collects the commenters as well? [YES/NO]: ")
                if self.collect_commenters.lower() == "yes":
                    self.collect_commenters = True
                else:
                    self.collect_commenters = False


            self.write_account_credentials()
            self.write_farming_options()
            self.write_browser_config()

            self.browser = Browser(self.browser_name, self.proxy, self.headless, self.user_agent)
            login_instagram()

    def login_instagram(self):
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        login_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'username']")))
        login_box.send_keys(self.email)

        pwd_box = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'password']")))
        pwd_box.send_keys(self.password)

        login_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@type = 'submit']")))
        login_button.click()
