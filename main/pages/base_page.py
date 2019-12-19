from selene.api import *

class BasePage():
    def __init__(self, driver, url = ""):
        self.driver = driver
        self.url = url

    def open(self):
        browser.open_url(self.url)
