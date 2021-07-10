from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from seleniumwire import webdriver
from .fetch import fetchUser as fetchUser_

class TwitterUser(object):

    # __CONSTRUCTOR
    def __init__(self, allowed_connection_retries=20, allowed_parsing_retries=500, headless=True):

        # allowed_connection_retries: AMOUNT OF TIMES ALLOWED TO RECOVER FROM AN ERROR DURING THE WEB REQUEST/SESSION.


        # # # PRIVATE METHODS/OBJECTS # # #
        
        # FIREFOX OPTIONS
        firefox_options                 = Options()
        if headless:
            firefox_options.add_argument("--headless")


        # # # PUBLIC METHODS/OBJECTS # # #
        
        # WEBDRIVER HARNESS
        self.driver                     = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

        # ALLOWED CONNECTION RETRIES
        self.allowed_connection_retries = allowed_connection_retries

        # ALLOWED PARSING RETRIES
        self.allowed_parsing_retries    = allowed_parsing_retries


    # FETCH-USER METHOD
    #@classmethod
    def fetchUser(self, screen_name):
        return fetchUser_(self, screen_name)

