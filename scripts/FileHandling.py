import os
from lxml import etree as ET
from UserStats import UserStats

class FileHandling():
    def __init__(self):
        super().__init__()

    def create_profile_folder(self):
        try:
            os.makedirs("Instats/Instats_Profiles/" + str(self.user_name))
        except FileExistsError:
            print(str(self.user_name) + " folder already exists")

    def print_profile_folders(self):
        path = "Instats/Instats_Profiles"
        dirs = os.listdir(path)

        for f in dirs:
            print(f)

    def write_browser_config(self):
        root = ET.Element("browser_config")

        browser         = ET.SubElement(root, "browser_name")
        browser.text    = self.browser_name
        proxy           = ET.SubElement(root, "proxy")
        proxy.text      = self.proxy
        headless        = ET.SubElement(root, "headless")
        headless.text   = str(self.headless)
        user_agent      = ET.SubElement(root, "user_agent")
        user_agent.text = str(self.user_agent)

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/browser_options.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_browser_config(self):
        tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) + "/browser_options.xml")
        root = tree.getroot()

        self.browser_name = root.find("browser_name").text
        self.proxy        = root.find("proxy").text

        if root.find("headless").text == "None" or "False":
            self.headless = False

        if root.find("headless").text == "None":
            self.user_agent = None

    def write_account_credentials(self):
        root = ET.Element("account_credentials")

        email         = ET.SubElement(root, "email")
        email.text    = self.email
        password      = ET.SubElement(root, "password")
        password.text = self.password

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/account_credentials.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_account_credentials(self):
        tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) +"/account_credentials.xml")
        root = tree.getroot()

        self.email    = root.find("email").text
        self.password = root.find("password").text

    def write_farming_options(self):
        root = ET.Element("farming_options")

        min_followers                = ET.SubElement(root, "min_followers")
        min_followers.text           = self.min_followers
        max_followers                = ET.SubElement(root, "max_followers")
        max_followers.text           = self.max_followers
        min_following                = ET.SubElement(root, "min_following")
        min_following.text           = self.min_following
        max_following                = ET.SubElement(root, "max_following")
        max_following.text           = self.max_following
        num_posts                    = ET.SubElement(root, "num_post")
        num_posts.text               = self.num_post
        follow_if_private            = ET.SubElement(root, "follow_if_private")
        follow_if_private.text       = str(self.follow_if_private)
        follow_if_empty              = ET.SubElement(root, "follow_if_empty")
        follow_if_empty.text         = str(self.follow_if_empty)
        follow_user                  = ET.SubElement(root, "follow_user")
        follow_user.text             = str(self.follow_user)
        follow_per_day               = ET.SubElement(root, "follow_per_day")
        follow_per_day.text          = str(self.follow_per_day)
        collect_commenters           = ET.SubElement(root, "collect_commenters")
        collect_commenters.text      = str(self.collect_commenters)
        number_of_likes              = ET.SubElement(root, "number_of_likes")
        number_of_likes.text         = self.number_of_likes
        actions_per_hour             = ET.SubElement(root, "actions_per_hour")
        actions_per_hour.text        = self.actions_per_hour

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/account_credentials.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_farming_options(self):
        tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) +"/farming_options.xml")
        root = tree.getroot()

        self.min_followers    = int(root.find("min_followers").text)
        self.max_followers    = int(root.find("max_followers").text)
        self.min_following    = int(root.find("min_following").text)
        self.max_following    = int(root.find("max_following").text)
        self.post_count       = int(root.find("num_post").text)
        self.actions_per_hour = int(root.find("actions_per_hour").text)
        self.number_of_likes  = int(root.find("number_of_likes").text)
        self.follow_per_day   = int(root.find("follow_per_day").text)

        if root.find("follow_if_private").text == "True":
            self.follow_if_private = True
        else:
            self.follow_if_private = False

        if root.find("follow_user").text == "True":
            self.follow_user = True
        else:
            self.follow_user = False

        if root.find("follow_if_empty").text == "True":
            self.follow_if_empty = True
        else:
            self.follow_if_empty = False

        if root.find("collect_commenters").text == "True":
            self.collect_commenters = True
        else:
            self.collect_commenters = False

    def write_follower_list(self):
        root = ET.Element("followers")

        for user in self.follower_list:
            user = ET.SubElement(root, "user")

            user_name          = ET.SubElement(user, "user_name")
            user_name.text     = user.user_name
            url                = ET.SubElement(user, "url")
            url.text           = user.url
            bio                = ET.SubElement(user, "bio")
            bio.text           = user.bio
            num_followers      = ET.SubElement(user, "num_followers")
            num_followers.text = user.num_followers
            num_following      = ET.SubElement(user, "num_following")
            num_following.text = user.num_following
            post_count         = ET.SubElement(user, "post_count")
            post_count.text    = user.post_count

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/followers.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_followers_list(self):
        try:
            tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) +"/followers.xml")
        except OSError:
            return 1

        root = tree.getroot()

        for user in root:
            user_profile = UserStats()

            user_profile.user_name     = user.find("user_name").text
            user_profile.url           = user.find("url").text
            user_profile.bio           = user.find("bio").text
            user_profile.num_followers = user.find("num_followers").text
            user_profile.num_following = user.find("num_following").text
            user_profile.post_count    = user.find("num_posts").text

            self.follower_list.append(user_profile)

    def write_following_list(self):
        root = ET.Element("following")

        for user in self.following_list:
            user = ET.SubElement(root, "user")

            user_name          = ET.SubElement(user, "user_name")
            user_name.text     = user.user_name
            url                = ET.SubElement(user, "url")
            url.text           = user.url
            bio                = ET.SubElement(user, "bio")
            bio.text           = user.bio
            num_followers      = ET.SubElement(user, "num_followers")
            num_followers.text = user.num_followers
            num_following      = ET.SubElement(user, "num_following")
            num_following.text = user.num_following
            post_count         = ET.SubElement(user, "post_count")
            post_count.text    = user.post_count

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/following.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_following_list(self):
        try:
            tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) +"/following.xml")
        except OSError:
            return 1

        root = tree.getroot()

        for user in root:
            user_profile = UserStats()

            user_profile.user_name     = user.find("user_name").text
            user_profile.url           = user.find("url").text
            user_profile.bio           = user.find("bio").text
            user_profile.num_followers = int(user.find("num_followers").text)
            user_profile.num_following = int(user.find("num_following").text)
            user_profile.post_count    = user.find("post_count").text

            self.following_list.append(user_profile)

    def write_non_followback_list(self):
        root = ET.Element("non_followback")

        for user in self.non_followback:
            user = ET.SubElement(root, "user")

            user_name          = ET.SubElement(user, "user_name")
            user_name.text     = user.user_name
            url                = ET.SubElement(user, "url")
            url.text           = user.url
            bio                = ET.SubElement(user, "bio")
            bio.text           = user.bio
            num_followers      = str(ET.SubElement(user, "num_followers"))
            num_followers.text = user.num_followers
            num_following      = str(ET.SubElement(user, "num_following"))
            num_following.text = user.num_following
            post_count         = ET.SubElement(user, "post_count")
            post_count.text    = str(user.post_count)

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/non_followback.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_non_followback_list(self):
        try:
            tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) +"/non_followback.xml")
        except OSError:
            return 1

        root = tree.getroot()

        for user in root:
            user_profile = UserStats()

            user_profile.user_name     = user.find("user_name").text
            user_profile.url           = user.find("url").text
            user_profile.bio           = user.find("bio").text
            user_profile.num_followers = int(user.find("num_followers").text)
            user_profile.num_following = int(user.find("num_following").text)
            user_profile.post_count    = int(user.find("post_count").text)

            self.non_followback.append(user_profile)

    def write_private_list(self):
        root = ET.Element("private")

        for user in self.private_list:
            user = ET.SubElement(root, "user")

            user_name          = ET.SubElement(user, "user_name")
            user_name.text     = user.user_name
            url                = ET.SubElement(user, "url")
            url.text           = user.url
            bio                = ET.SubElement(user, "bio")
            bio.text           = user.bio
            num_followers      = ET.SubElement(user, "num_followers")
            num_followers.text = str(user.num_followers)
            num_following      = ET.SubElement(user, "num_following")
            num_following.text = str(user.num_following)
            post_count         = ET.SubElement(user, "post_count")
            post_count.text    = str(user.post_count)

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/private.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_private_list(self):
        try:
            tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) +"/private.xml")
        except OSError:
            return 1

        root = tree.getroot()

        for user in root:
            user_profile = UserStats()

            user_profile.user_name     = user.find("user_name").text
            user_profile.url           = user.find("url").text
            user_profile.bio           = user.find("bio").text
            user_profile.num_followers = int(user.find("num_followers").text)
            user_profile.num_following = int(user.find("num_following").text)
            user_profile.post_count    = int(user.find("post_count").text)

            self.private_list.append(user_profile)
