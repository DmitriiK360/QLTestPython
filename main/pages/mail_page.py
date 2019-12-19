from .base_page import BasePage
from selene.api import *

class MailPage(BasePage):

    WRITE_EMAIL_BUTTON = s(by.xpath("//div[contains(@class, 'sidebar__compose-btn-box')]"))
    TO_INPUT = s(by.xpath("//div[contains(@class, 'head_container')]//input"))
    SUBJECT_INPUT = s(by.xpath("//div[contains(@class, 'subject__container')]//input"))
    BODY_INPUT = s(by.xpath("//div[contains(@class, 'cke_widget_wrapper')]/preceding-sibling::*[2]"))
    SEND_EMAIL_BUTTON = s(by.xpath("//span[contains(@title, 'Отправить')]"))
    MAIL_SENT_MESSAGE = s(by.xpath("//div[@class='layer-sent-page']//span[text()='отправлено']"))
    LOGOUT_BUTTON = s(by.id("PH_logoutLink"))

    def click_write_email_button(self):
        self.WRITE_EMAIL_BUTTON.click()

    def set_to_input(self, text):
        self.TO_INPUT.set(text)

    def get_text_to_input(self):
        return self.TO_INPUT.get_attribute("value")

    def set_subject_input(self, subject):
        self.SUBJECT_INPUT.set(subject)

    def get_text_subject_input(self):
        return self.SUBJECT_INPUT.get_attribute("value")

    def set_body_input(self, body):
        self.BODY_INPUT.set(body)

    def get_text_body_input(self):
        return self.BODY_INPUT.text

    def click_send_email_button(self):
        self.SEND_EMAIL_BUTTON.click()

    def click_logout_button(self):
        self.LOGOUT_BUTTON.click()

    def is_page_opened(self):
        return self.WRITE_EMAIL_BUTTON.is_displayed()

    def is_email_sent(self):
        return self.MAIL_SENT_MESSAGE.is_displayed()