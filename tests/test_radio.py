from selenium.webdriver import Chrome
import pytest
from pages.radio import Radio

@pytest.fixture()
def browser():
    driver = Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# verifies that the No option is disabled on page load
def test_no_disabled(browser):
    page = Radio(browser)
    page.load()
    assert not page.check_no()

# verifies that the Yes option is enabled on page load
def test_yes_enabled(browser):
    page = Radio(browser)
    page.load()
    assert page.check_yes()

def test_impressive_enabled(browser):
    page = Radio(browser)
    page.load()
    assert page.check_impressive()

def test_select_yes(browser):
    page = Radio(browser)
    page.load()
    page.select_yes()

