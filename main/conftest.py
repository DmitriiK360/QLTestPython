import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser():
    print("\nStart driver for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nQuit driver..")
    driver.quit()