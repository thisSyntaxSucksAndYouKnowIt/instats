from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

class Browser(webdriver.Firefox, webdriver.Chrome):
    def __init__(self):
        self.browser_name = None
        self.proxy        = None
        self.user_agent   = None
        self.headless     = None

    def create_browser_firefox(self):
        fox_options  = FirefoxOptions()
        fox_proxy    = None
        capabilities = None

        if self.headless == False:
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

        if self.headless == False:
            chr_options.add_argument("headless")

        if self.proxy:
            chr_options.add_argument('--proxy-server=%s' % self.proxy)

        webdriver.Chrome.__init__(self, chrome_options = chr_options)

    def restart_browser(self):
        self.close()
        #include change options then restart a new browser
