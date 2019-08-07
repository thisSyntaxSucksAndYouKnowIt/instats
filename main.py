from actions import *
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import getpass
import time
from farming import *
from tui import *

if __name__ == '__main__':

    clear_screen()
    title_screen()

    '''
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

    '''
    usr_list = []
    usr_sorted = []
    followers_list = []
    following_list = []
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

    notifications_popup(driver)
    time.sleep(1)
    go_to_profile(driver)
    time.sleep(2)

    instats_init(driver)

    while is_on == True:

        clear_screen()
        title_screen()
        print("Instats temp menu")
        print("Options:")
        print("a: farm likers from specific post")
        print("b: sort users from likers farmed " + str(len(usr_list)))
        print("c: mass like from likers list " + str(len(usr_sorted)))
        print("d: farm followers from profile")
        print("e: farm following from profile")
        print("q: quit")

        choice = input("Choice: ")

        if choice == 'a':
            clear_screen()
            title_screen()

            url = input("Enter url from the post you want to scrape: ")
            driver.get(url)
            number = input("Enter number of profiles you want to scrape " +str(get_number_of_likers(driver))+" available: ")
            number = int(number)
            if number > get_number_of_likers(driver):
                number = get_number_of_likers(driver)

            usr_list = collect_likers(driver, number)


        if choice == 'b':
            usr_sorted = sort_profiles(driver, usr_list)


        if choice == 'c':
            mass_like(driver, usr_sorted, 2)


        if choice == 'd':
            clear_screen()
            title_screen()

            profile = input("Which profile you want to collect followers from? ")
            driver.get("https://www.instagram.com/" + profile)
            time.sleep(2)

            create_profile_folders(driver)
            followers_list = collect_followers(driver)

            write_file("Instats_Profiles/" + str(profile) + "followers.txt", followers_list)

        if choice == 'e':
            clear_screen()
            title_screen()

            profile = input("Which profile you want to collect followings from? ")
            driver.get("https://www.instagram.com/" + profile)
            time.sleep(2)

            create_profile_folders(driver)

            following_list = collect_following(driver)

            write_file("Instats_Profiles/" + str(profile) + "following.txt", following_list)

        if choice == 'q':
            driver.close()
            is_on = False
