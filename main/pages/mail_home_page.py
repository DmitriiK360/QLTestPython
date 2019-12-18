from selenium.webdriver.common.by import By
from .base_page import BasePage

class MailHomePage(BasePage):

    MAIL_INPUT = (By.ID, "mailbox:login")
    PASSWORD_INPUT = (By.ID, "mailbox:password")
    TYPE_PASSWORD_BUTTON = (By.XPATH, "//label[contains(@id, 'mailbox:submit') and text() = 'Ввести пароль']")
    LOGIN_BUTTON = (By.XPATH, "//label[contains(@id, 'mailbox:submit') and text() = 'Войти']")
    SEARCH_INPUT = (By.ID, "q")

    def set_mail(self, text):
        element = self.find_element(self.MAIL_INPUT)
        #element.click()
        element.clear()
        element.send_keys(text)

    def get_text_email(self):
        element = self.find_element(self.MAIL_INPUT)
        return element.get_attribute("value")

    def click_type_password_button(self):
        element = self.find_element(self.TYPE_PASSWORD_BUTTON)
        element.click()

    def set_password(self, text):
        element = self.find_element(self.PASSWORD_INPUT)
        #element.click()
        element.clear()
        element.send_keys(text)

    def get_text_password(self):
        element = self.find_element(self.PASSWORD_INPUT)
        return element.get_attribute("value")

    def click_login_button(self):
        element = self.find_element(self.LOGIN_BUTTON)
        element.click()

    def is_page_opened(self):
        element = self.find_element(self.SEARCH_INPUT)
        return element.is_displayed()