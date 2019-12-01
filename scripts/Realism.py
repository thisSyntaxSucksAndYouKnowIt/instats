from selenium.webdriver.common.keys import Keys
import random
import time

class Realism:
    def __init__(self):
        pass

    def random_number(self):
        return random.randint(1, 80) / 295

    def scroll_down(self):
        for n in range(0, random.randrange(7,9)):
            time.sleep(random.uniform(0.003, 0.008))
            self.execute_script("window.scrollBy(0,"+str(random.uniform(40,45))+")")

    def scroll_up(self):
        for n in range(random.randrange(-9,-7), 0):
            time.sleep(random.uniform(0.003, 0.008))
            self.execute_script("window.scrollBy(0,"+str(random.uniform(-40,-45))+")")

    def realistic_typing(self, box, string):
        initial_wait = False
        box.click()

        if initial_wait == False:
            time.sleep(random.randrange(1,2))
            initial_wait = True

        for char in string:
            delay = self.random_number()
            box.send_keys(char)
            time.sleep(delay)
