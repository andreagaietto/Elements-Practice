from selenium.webdriver import Chrome
import pytest

# runs prior to each test
@pytest.fixture()
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def