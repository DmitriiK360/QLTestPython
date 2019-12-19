import pytest
from selenium import webdriver
from selene.browser import set_driver, driver

@pytest.fixture(scope="module")
def browser():
    print("\nStart driver for test..")
    set_driver(webdriver.Chrome())
    driver().implicitly_wait(20)
    driver().maximize_window()
    yield driver
    print("\nQuit driver..")
    driver().quit()