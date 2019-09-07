from selenium.webdriver.common.keys import Keys
import random
import time
import datetime

def random_number():
    return random.randint(1, 80) / 295

def timing_act(min_num, max_num):
    return random.randrange(min_num, max_num)

def realistic_typing(box, string):
    random.seed(datetime.datetime.now())

    for char in string:
        delay = random_number()
        box.send_keys(char)
        time.sleep(delay)
