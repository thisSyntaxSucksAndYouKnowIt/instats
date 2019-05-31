from actions import *
from selenium.webdriver.firefox.options import Options as FirefoxOptions

if __name__ == '__main__':
    #download geckodriver and chromedriver and copy them to /usr/local/bin
    #chmod a+x chromedriver needed for chromedriver to work at all

    '''
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    '''

    #options = webdriver.ChromeOptions()
    #options.add_argument("headless")
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")



