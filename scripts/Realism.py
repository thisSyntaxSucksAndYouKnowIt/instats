from selenium.webdriver.common.keys import Keys
import random
import time
import datetime

class Realism:
    def __init__(self):
        pass

    def random_number(self):
        return random.randint(1, 80) / 295

    def timing_act(self, min_num, max_num):
        return random.randrange(min_num, max_num)

    def scroll_down(self):
        for n in range(0, random.randrange(7,9)):
            time.sleep(random.uniform(0.003, 0.008))
            self.execute_script("window.scrollBy(0,"+str(random.uniform(40,45))+")")

    def scroll_up(self):
        for n in range(random.randrange(-9,-7), 0):
            time.sleep(random.uniform(0.003, 0.008))
            self.execute_script("window.scrollBy(0,"+str(random.uniform(-40,-45))+")")

    def realistic_typing(self, box, string):
        random.seed(datetime.datetime.now())

        for char in string:
            delay = random_number()
            box.send_keys(char)
            time.sleep(delay)
