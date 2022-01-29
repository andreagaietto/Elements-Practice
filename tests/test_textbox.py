from selenium.webdriver import Chrome
import pytest
from pages.textbox import TextBox

# runs prior to each test
@pytest.fixture()
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_no_input(browser):
    page = TextBox(browser)
    page.load()
    page.click_submit()
    assert not len(browser.find_elements_by_id('name'))

def test_single_name(browser):
    page = TextBox(browser)
    page.load()
    page.enter_name('John')
    page.click_submit()
    assert page.return_name()

def test_two_name(browser):
    page = TextBox(browser)
    page.load()
    page.enter_name('John Smith')
    page.click_submit()