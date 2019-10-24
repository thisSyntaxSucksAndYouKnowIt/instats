from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

class Browser(webdriver.Firefox, webdriver.Chrome):
    def __init__(self, browser, proxy, headless, user_agent):
        self.browser_name = browser
        self.proxy        = proxy
        self.user_agent   = user_agent
        self.headless     = headless

        if self.browser_name == "Firefox":
            self.create_browser_firefox()

        elif self.browser_name == "Chrome":
            self.create_browser_chrome()

    def create_browser_firefox(self):
        fox_options  = FirefoxOptions()
        fox_proxy    = None
        capabilities = None

        if self.headless == True:
            fox_options.add_argument("--headless")

        if self.proxy:
            fox_proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': self.proxy,
                'ftpProxy' : self.proxy,
                'sslProxy' : self.proxy,
                'noProxy'  : None})

            capabilities = webdriver.DesiredCapabilities.FIREFOX
            fox_proxy.add_to_capabilities(capabilities)

        webdriver.Firefox.__init__(self, options = fox_options, desired_capabilities = capabilities)

    def create_browser_chrome(self):
        chr_options  = ChromeOptions()
        capabilities = None

        if self.headless == True:
            chr_options.add_argument("headless")

        if self.proxy:
            chr_options.add_argument('--proxy-server=%s' % self.proxy)

        webdriver.Chrome.__init__(self, chrome_options = chr_options)

    def restart_browser(self):
        self.close()
        #include change options then restart a new browser
