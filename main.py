from actions import *
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import getpass
import time
from farming import *

if __name__ == '__main__':
    '''
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

    '''
    usr_list = []
    is_on = True

    name = input("Enter mail: ")
    pwd = getpass.getpass("Enter pass: ")
    #options = webdriver.ChromeOptions()
    #options.add_argument("headless")

    #driver = webdriver.Chrome(chrome_options = options)
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

    login_insta(driver, name, pwd)
    time.sleep(3)

    while is_on == True:
        print("Instats temp menu")
        print("Options:")
        print("a: farm likers from specific post")
        print("b: sort users from likers farmed")
        print("c: mass like from likers list")
        print("q: quit")

        choice = input("Choice: ")

        if choice == 'a':
            url = input("Enter url from the post you want to scrape: ")
            driver.get(url)
            number = input("Enter number of profiles you want to scrape " +str(get_number_of_likers(driver))+" available: ")
            number = int(number)
            if number > get_number_of_likers(driver):
                number = get_number_of_likers(driver)

            usr_list = collect_likers(driver, number)


        if choice == 'q':
            driver.close()
            is_on = False
