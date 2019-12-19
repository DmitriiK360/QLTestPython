from selene.api import *
from .base_page import BasePage

class MailHomePage(BasePage):

    MAIL_INPUT = s(by.id("mailbox:login"))
    PASSWORD_INPUT = s(by.id("mailbox:password"))
    TYPE_PASSWORD_BUTTON = s(by.xpath("//label[contains(@id, 'mailbox:submit') and text() = 'Ввести пароль']"))
    LOGIN_BUTTON = s(by.xpath("//label[contains(@id, 'mailbox:submit') and text() = 'Войти']"))
    SEARCH_INPUT = s(by.id("q"))

    def set_mail(self, text):
        self.MAIL_INPUT.set(text)

    def get_text_email(self):
        return self.MAIL_INPUT.get_attribute("value")

    def click_type_password_button(self):
        self.TYPE_PASSWORD_BUTTON.click()

    def set_password(self, text):
        self.PASSWORD_INPUT.set(text)

    def get_text_password(self):
        return self.PASSWORD_INPUT.get_attribute("value")

    def click_login_button(self):
        self.LOGIN_BUTTON.click()

    def is_page_opened(self):
        return self.SEARCH_INPUT.is_displayed()