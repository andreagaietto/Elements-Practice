from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TextBox:

    URL = "https://demoqa.com/text-box"
    NAME_FIELD = (By.ID, 'userName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    SUBMIT = (By.ID, 'submit')
    NAME_RETURN = (By.ID, 'name')
    EMAIL_RETURN = (By.ID, 'email')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def enter_name(self, name):
        name_input = self.browser.find_element(*self.NAME_FIELD)
        name_input.send_keys(name)

    def click_submit(self):
        submit_button = self.browser.find_element(*self.SUBMIT)
        submit_button.click()

    def return_name(self):
        name_return = self.browser.find_element(*self.NAME_RETURN)
        return name_return.text

    def enter_email(self, email):
        email_input = self.browser.find_element(*self.EMAIL_FIELD)
        email_input.send_keys(email)

    def return_email(self):
        email_return = self.browser.find_element(*self.EMAIL_RETURN)
        return email_return.text