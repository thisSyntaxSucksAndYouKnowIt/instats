from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

def remove_char(string, char):
    return re.sub(char,"", string)

def to_int(string):
    return int(string)

def login_insta():
    #//input[@name = 'username']
    #//input[@name = 'password']
    #//button[@type = 'submit']

def notifications_popup():
    #//button[contains(text(), 'Not Now')]
    #//button[contains(text(), 'Turn On')]

def go_to_profile()
    #//span[@aria-label = 'Profile']

def get_username():
    #//div[@class = 'nZSzR']/h1

def get_postcount():
    #//li[@class = 'Y8-fY'][1]/a/span

def get_followers():
    #//li[@class = 'Y8-fY'][2]/a/span

def get_following():
    #//li[@class = 'Y8-fY'][3]/a/span

def is_empty():
    #//div[@class = 'v1Nh3 kIKUG _bz0w']

def like_picture():
    #//span[@aria-label = 'Like']

def dislike_picture():
    #//span[@aria-label = 'Unlike']

def comment_post():
    #//textarea[@aria-label = 'Add a comment…']
    #//button[@type = 'submit']

