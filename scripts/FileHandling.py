import os
from lxml import etree as ET
from UserStats import UserStats

class FileHandling():
    def __init__(self):
        super().__init__()

    def create_profile_folders(self):
        try:
            os.makedirs("Instats/Instats_Profiles/" + str(self.user_name))
        except FileExistsError:
            print(str(self.user_name) + ".txt folder already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/account_credentials.xml")
        except FileExistsError:
            print("account_credentials.xml file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/account_stats.txt")
        except FileExistsError:
            print("account_stats.txt file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/browser_options.xml")
        except FileExistsError:
            print("browser_options.xml file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/farming_options.txt")
        except FileExistsError:
            print("farming_options.txt file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/followers.txt")
        except FileExistsError:
            print("followers.txt file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/following.txt")
        except FileExistsError:
            print("following.txt file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/followers_clean.txt")
        except FileExistsError:
            print("followers_clean.txt file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/following_clean.txt")
        except FileExistsError:
            print("following_clean.txt file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/non_followback.txt")
        except FileExistsError:
            print("non_followback.txt file already exists")

        try:
            os.mknod("Instats/Instats_Profiles/" + str(self.user_name) + "/unavailable.txt")
        except FileExistsError:
            print("unavailable.txt file already exists")

    def write_to_file(self, path, user_list):
        f = open(path, "a+")

        for usr in user_list:
            if is_already_in(path, usr) == False:
                if '\n' in usr:
                    f.write(profile)
                else:
                    f.write(profile + '\n')
        f.close()

    def is_already_in(path, user):
        with open(path) as f:
            lines = f.readlines()

        for line in lines:
            if user in line:
                return True
        return False

    def write_browser_config(self):
        root = ET.Element("browser_config")

        browser = ET.SubElement(root, "browser")
        browser.text = self.browser_name

        proxy = ET.SubElement(root, "proxy")
        proxy.text = self.proxy

        headless = ET.SubElement(root, "headless")
        headless.text = str(self.headless)

        user_agent = ET.SubElement(root, "user_agent")
        user_agent.text = str(self.user_agent)

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/browser_options.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_browser_config(self):
        tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) + "/browser_options.xml")
        root = tree.getroot()

        self.browser    = root.find("browser").text
        self.proxy      = root.find("proxy").text

        if root.find("headless").text == "None" or "False":
            self.headless = False

        if root.find("headless").text == "None":
            self.user_agent = None

    def write_account_credentials(self):
        root = ET.Element("account_credentials")

        email = ET.SubElement(root, "email")
        email.text = self.email

        password = ET.SubElement(root, "password")
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

        min_followers = ET.SubElement(root, "min_followers")
        min_followers.text = self.min_followers

        max_followers = ET.SubElement(root, "max_followers")
        max_followers .text = self.max_followers

        min_following = ET.SubElement(root, "min_following")
        min_following.text = self.min_following

        max_following = ET.SubElement(root, "max_following")
        max_following.text = self.max_following

        num_posts = ET.SubElement(root, "num_post")
        num_posts.text = self.num_post

        is_private = ET.SubElement(root, "is_private")
        is_private.text = str(self.is_private)

        is_empty = ET.SubElement(root, "is_empty")
        is_empty.text = str(self.is_empty)

        actions_per_hour = ET.SubElement(root, "actions_per_hour")
        actions_per_hour.text = str(self.actions_per_hour)

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/account_credentials.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_farming_options(self):
        tree = ET.parse("Instats/Instats_Profiles/"+ str(self.user_name) +"/farming_options.xml")
        root = tree.getroot()

        self.min_followers    = root.find("min_followers").text
        self.max_followers    = root.find("max_followers").text
        self.min_following    = root.find("min_following").text
        self.max_following    = root.find("max_following").text
        self.num_post         = root.find("num_post").text
        self.actions_per_hour = root.find("actions_per_hour").text

        if root.find("is_private").text == "True":
            self.is_private = True
        else:
            self.is_private = False

        if root.find("is_empty").text == "True":
            self.is_empty = True
        else:
            self.is_empty = False

    def write_follower_list(self):
        root = ET.Element("followers")

        for user in self.follower_list:
            user = ET.SubElement(root, "user")

            user_name = ET.SubElement(user, "user_name")
            user_name.text = user.user_name

            url = ET.SubElement(user, "url")
            url.text = user.url

            bio = ET.SubElement(user, "bio")
            bio.text = user.bio

            num_followers = ET.SubElement(user, "num_followers")
            num_followers.text = user.num_followers

            num_following = ET.SubElement(user, "num_following")
            num_following.text = user.num_following

            num_posts = ET.SubElement(user, "num_posts")
            num_posts.text = user.num_posts

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/followers.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_followers_list(self):
        pass

    def write_following_list(self):
        root = ET.Element("following")

        for user in self.following_list:
            user = ET.SubElement(root, "user")

            user_name = ET.SubElement(user, "user_name")
            user_name.text = user.user_name

            url = ET.SubElement(user, "url")
            url.text = user.url

            bio = ET.SubElement(user, "bio")
            bio.text = user.bio

            num_followers = ET.SubElement(user, "num_followers")
            num_followers.text = user.num_followers

            num_following = ET.SubElement(user, "num_following")
            num_following.text = user.num_following

            num_posts = ET.SubElement(user, "num_posts")
            num_posts.text = user.num_posts

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/following.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_following_list(self):
        pass

    def load_non_followback_list(self):
        pass

    def write_non_followback_list(self):
        root = ET.Element("non_followback")

        for user in self.non_followback:
            user = ET.SubElement(root, "user")

            user_name = ET.SubElement(user, "user_name")
            user_name.text = user.user_name

            url = ET.SubElement(user, "url")
            url.text = user.url

            bio = ET.SubElement(user, "bio")
            bio.text = user.bio

            num_followers = ET.SubElement(user, "num_followers")
            num_followers.text = user.num_followers

            num_following = ET.SubElement(user, "num_following")
            num_following.text = user.num_following

            num_posts = ET.SubElement(user, "num_posts")
            num_posts.text = user.num_posts

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/non_followback.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")

    def load_private_list(self):
        pass

    def write_private_list(self):
        root = ET.Element("private")

        for user in self.private_list:
            user = ET.SubElement(root, "user")

            user_name = ET.SubElement(user, "user_name")
            user_name.text = user.user_name

            url = ET.SubElement(user, "url")
            url.text = user.url

            bio = ET.SubElement(user, "bio")
            bio.text = user.bio

            num_followers = ET.SubElement(user, "num_followers")
            num_followers.text = user.num_followers

            num_following = ET.SubElement(user, "num_following")
            num_following.text = user.num_following

            num_posts = ET.SubElement(user, "num_posts")
            num_posts.text = user.num_posts

        tree = ET.ElementTree(root)
        tree.write("Instats/Instats_Profiles/"+ str(self.user_name) +"/private.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")
