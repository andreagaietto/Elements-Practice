from selenium.webdriver import Chrome
import pytest
from pages.textbox import TextBox


# runs prior to each test
@pytest.fixture()
def browser():
    driver = Chrome()
    driver.implicitly_wait(8)
    yield driver
    driver.quit()

# verify that nothing appears when submitting a blank form
def test_no_input(browser):
    page = TextBox(browser)
    page.load()
    page.click_submit()
    assert not len(browser.find_elements_by_id('name'))

# verify that a single name is returned properly
def test_single_name(browser):
    page = TextBox(browser)
    page.load()
    page.enter_name('John')
    page.click_submit()
    assert page.return_name() == 'Name:John'

# verify that a formal name is returned properly
def test_two_name(browser):
    page = TextBox(browser)
    page.load()
    page.enter_name('John Smith')
    page.click_submit()
    assert page.return_name() == 'Name:John Smith'

# verify that if only a correct email is entered on the form, it is returned properly
def test_valid_email_only(browser):
    page = TextBox(browser)
    page.load()
    page.enter_email("john@example.com")
    page.click_submit()
    assert page.return_email() == 'Email:john@example.com'

#verify that if only a incorrect email is entered, error is displayed and the email is not accepted
def test_invalid_email_only(browser):
    page = TextBox(browser)
    page.load()
    page.enter_email('john')
    page.click_submit()
    assert browser.find_element_by_class_name('field-error').is_displayed()
    assert not len(browser.find_elements_by_id('email'))