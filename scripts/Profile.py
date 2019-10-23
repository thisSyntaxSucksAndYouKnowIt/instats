from Farming import Farming
from FileHandling import FileHandling
from Browser import Browser

class Profile(Farming, FileHandling):
    def __init__(self, user_name, login, passwd, browser, proxy, headless, usr_agent):
        #Account credentials
        self.email    = login
        self.password = passwd

        #Browser options
        self.browser_name = browser
        self.proxy        = proxy
        self.headless     = headless
        self.user_agent   = usr_agent
        self.browser      = None

        #Account infos
        self.user_name   = user_name
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
        self.min_followers    = None
        self.max_followers    = None
        self.min_following    = None
        self.max_following    = None
        self.num_post         = None
        self.is_private       = None
        self.is_empty         = None
        self.actions_per_hour = None

    def initialize_profile(self):
        self.browser = Browser(self.browser_name, self.proxy, self.headless, self.user_agent)


