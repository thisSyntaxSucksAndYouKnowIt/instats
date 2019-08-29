from actions import *
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import getpass
import time
from farming import *
from tui import *
from structs import *

if __name__ == '__main__':

    instats_init()

    clear_screen()
    title_screen()

    '''
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    '''

    list_obj = lists()

    is_on = True

    name = input(" Enter mail: ")
    pwd = getpass.getpass(" Enter pass: ")
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

    while is_on == True:

        clear_screen()
        title_screen()
        main_menu(list_obj)

        choice = input(" Choice: ")

        if choice == 'a':
            clear_screen()
            title_screen()

            url = input(" Enter url from the post you want to scrape: ")
            driver.get(url)
            number = input(" Enter number of profiles you want to scrape " +str(get_number_of_likers(driver))+" available: ")
            number = int(number)
            if number > get_number_of_likers(driver):
                number = get_number_of_likers(driver)

            list_obj = collect_likers(driver, number, list_obj)

        if choice == 'b':
            list_obj = sort_profiles(driver, list_obj, 1)

        if choice == 'c':
            mass_like(driver, list_obj, 2)

        if choice == 'd':
            clear_screen()
            title_screen()

            profile = None

            if list_obj.user_name_post != None:
                choice = input(" Do you want to farm the followers of the user you farmed likers from? yes/no: ")
                if choice == "yes":
                    profile = list_obj.user_name_post

            else:
                profile = input(" Which profile you want to collect followers from? (Enter the username): ")

            driver.get("https://www.instagram.com/" + profile)
            time.sleep(2)

            create_profile_folders(driver)
            list_obj = collect_followers(driver,list_obj)

            write_file("Instats/Instats_Profiles/" + str(profile) + "/followers.txt", list_obj.followers_collected)

        if choice == 'e':
            list_obj = sort_profiles(browser, list_obj, 2)
            write_file("Instats/Instats_Profiles/" + str(list_obj.user_name_followers) + "/clean_followers.txt", list_obj.followers_collected_clean)

        if choice == 'f':
            clear_screen()
            title_screen()

            profile = None

            if list_obj.user_name_post != None:
                choice = input(" Do you want to farm the following of the user you farmed likers from? yes/no: ")
                if choice == "yes":
                    profile = list_obj.user_name_post

            else:
                profile = input(" Which profile you want to collect followings from? (Enter the username): ")

            driver.get("https://www.instagram.com/" + profile)
            time.sleep(2)

            create_profile_folders(driver)
            list_obj = collect_following(driver, list_obj)

            write_file("Instats/Instats_Profiles/" + str(profile) + "/following.txt", list_obj.following_collected)

        if choice == 'g':
            list_obj = sort_profiles(browser, list_obj, 3)
            write_file("Instats/Instats_Profiles/" + str(list_obj.user_name_following) + "/clean_following.txt", list_obj.following_collected_clean)

        if choice == 'h':
            list_obj = load_file("Instats/Instats_Profiles/fancyfashinsta/followers.txt",list_obj, 1, False)

        if choice == 'i':
            list_obj = load_file("Instats/Instats_Profiles/fancyfashinsta/following.txt",list_obj, 2, False)

        if choice == 'j':
            list_obj = load_file("Instats/Instats_Profiles/fancyfashinsta/followers.txt",list_obj, 1, False)
            list_obj = load_file("Instats/Instats_Profiles/fancyfashinsta/following.txt",list_obj, 2, False)
            list_obj = find_non_followback(list_obj)

            write_file("Instats/Instats_Profiles/fancyfashinsta/followers.txt", list_obj.non_follow_back)

        if choice == 'q':
            driver.close()
            clear_screen()
            print(" Goodbye and thank you for chosing Instats to help you grow your account!")
            is_on = False
