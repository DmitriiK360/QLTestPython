from main.pages.mail_home_page import MailHomePage

def test_guest_can_go_to_login_page(browser):
    link = "http://mail.ru"
    mail_home_page = MailHomePage(browser, link)
    mail_home_page.open()
    mail_home_page.set_mail_input("login")
