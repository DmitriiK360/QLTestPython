from selenium.webdriver.common.by import By
from .base_page import BasePage

class MailPage(BasePage):

    WRITE_EMAIL_BUTTON = (By.XPATH, "//div[contains(@class, 'sidebar__compose-btn-box')]")
    TO_INPUT = (By.XPATH, "//div[contains(@class, 'head_container')]//input")
    SUBJECT_INPUT = (By.XPATH, "//div[contains(@class, 'subject__container')]//input")
    BODY_INPUT = (By.XPATH,"//div[contains(@class, 'editable-container')]/div/div/div[1]")
    SEND_EMAIL_BUTTON = (By.XPATH, "//span[contains(@title, 'Отправить')]")
    MAIL_SENT_MESSAGE = (By.XPATH, "//div[@class='layer-sent-page']//span[text()='отправлено']")
    LOGOUT_BUTTON = (By.ID, "PH_logoutLink")

    def click_write_email_button(self):
        element = self.find_element(self.WRITE_EMAIL_BUTTON)
        element.click()

    def set_to_input(self, text):
        element = self.find_element(self.TO_INPUT)
        element.clear()
        element.send_keys(text)

    def get_text_to_input(self):
        element = self.find_element(self.TO_INPUT)
        return element.get_attribute("value")

    def set_subject_input(self, subject):
        element = self.find_element(self.SUBJECT_INPUT)
        element.clear()
        element.send_keys(subject)

    def get_text_subject_input(self):
        element = self.find_element(self.SUBJECT_INPUT)
        return element.get_attribute("value")

    def set_body_input(self, body):
        element = self.find_element(self.BODY_INPUT)
        element.clear()
        element.send_keys(body)

    def get_text_body_input(self):
        element = self.find_element(self.BODY_INPUT)
        return element.text

    def click_send_email_button(self):
        element = self.find_element(self.SEND_EMAIL_BUTTON)
        return element.click()

    def click_logout_button(self):
        element = self.find_element(self.LOGOUT_BUTTON)
        return element.click()

    def is_page_opened(self):
        element = self.find_element(self.WRITE_EMAIL_BUTTON)
        return element.is_displayed()

    def is_email_sent(self):
        element = self.find_element(self.MAIL_SENT_MESSAGE)
        return element.is_displayed()