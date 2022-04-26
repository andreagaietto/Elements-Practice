from selenium.webdriver import Chrome
import pytest
from pages.textbox import TextBox
import pytest_check as check

# runs prior to each test
@pytest.fixture()
def browser():
    driver = Chrome()
    driver.implicitly_wait(5)
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

# verify that if only an incorrect email is entered, error is displayed and the email is not accepted
def test_invalid_email_only(browser):
    page = TextBox(browser)
    page.load()
    page.enter_email('john')
    page.click_submit()
    assert browser.find_element_by_class_name('field-error').is_displayed()
    assert not len(browser.find_elements_by_id('email'))

# verify that correct address is returned from the current address field
def test_valid_current_address(browser):
    page = TextBox(browser)
    page.load()
    page.enter_current_address("10280 Test Road Test City, 27513")
    page.click_submit()
    assert page.return_current_address() == 'Current Address :10280 Test Road Test City, 27513'

# verify correct placeholder text is displayed in the current address box
def test_current_address_placeholder(browser):
    page = TextBox(browser)
    page.load()
    assert page.return_current_address_placeholder() == 'Current Address'

# verify permanent address field doesn't have placeholder text
def test_perm_address_placeholder(browser):
    page = TextBox(browser)
    page.load()
    assert not page.return_perm_address_placeholder()

# verify value returned by the permanent address field
def test_perm_address(browser):
    page = TextBox(browser)
    page.load()
    page.enter_perm_address('10230 Test Street')
    page.click_submit()
    assert page.return_perm_address() == 'Permananet Address :10230 Test Street'

# verify entire form, returns detailed results for each check
def test_entire_form(browser):
    page = TextBox(browser)
    page.load()
    page.enter_name('John Smith')
    page.enter_email("john@example.com")
    page.enter_current_address("10280 Test Road Test City, 27513")
    page.enter_perm_address('10230 Test Street')
    page.click_submit()
    check.equal(page.return_name(), 'Name:John Smith')
    check.equal(page.return_email(), 'Email:john@example.com')
    check.equal(page.return_current_address(), 'Current Address :10280 Test Road Test City, 27513')
    check.equal(page.return_perm_address(), 'Permananet Address :10230 Test Street')