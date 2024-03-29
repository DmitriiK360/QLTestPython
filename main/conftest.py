import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    print("\nStart driver for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    print("\nQuit driver..")
    driver.quit()