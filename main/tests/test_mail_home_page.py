from main.constants.properties import Properties
from main.pages.mail_home_page import MailHomePage
from main.pages.mail_page import MailPage

def test_login_mail(browser):
    mail_home_page = MailHomePage(browser, Properties.URL_MAIL_RU)
    mail_home_page.open()

    assert mail_home_page.is_page_opened(), "Mail.ru home page doesn't open."

    mail_home_page.set_mail(Properties.LOGIN_MAIL_RU)

    assert mail_home_page.get_text_email() == Properties.LOGIN_MAIL_RU

    mail_home_page.click_type_password_button()
    mail_home_page.set_password(Properties.PASSWORD_MAIL_RU)

    assert mail_home_page.get_text_password() == Properties.PASSWORD_MAIL_RU

    mail_home_page.click_login_button()


def test_send_email(browser):
    #set variables
    send_to = Properties.LOGIN_MAIL_RU + "@mail.ru";
    subject_text = "test subject";
    body_text = "test body";

    mail_page = MailPage(browser)

    assert mail_page.is_page_opened(), "Mail page doesn't open."

    mail_page.click_write_email_button()
    mail_page.set_to_input(send_to)
    assert mail_page.get_text_to_input() == send_to

    mail_page.set_subject_input(subject_text)
    assert mail_page.get_text_subject_input() == subject_text

    mail_page.set_body_input(body_text)
    assert mail_page.get_text_body_input() == body_text

    mail_page.click_send_email_button()
    assert mail_page.is_email_sent(), "Email not sent."

    mail_page.click_logout_button()