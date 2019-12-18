from selenium.webdriver.common.by import By
from .base_page import BasePage

class MailHomePage(BasePage):

    MAIL_INPUT = (By.ID, "mailbox:login")
    PASSWORD_INPUT = (By.ID, "mailbox:password")

    def set_mail_input(self, text):
        search_field = self.find_element(self.MAIL_INPUT)
        search_field.click()
        search_field.send_keys(text)

    def set_password_input(self, text):
        search_field = self.find_element(self.PASSWORD_INPUT)
        search_field.click()
        search_field.send_keys(text)

