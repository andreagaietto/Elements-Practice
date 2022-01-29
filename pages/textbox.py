from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TextBox:

    URL = "https://demoqa.com/text-box"
    NAME_FIELD = (By.ID, 'userName')
    SUBMIT = (By.ID, 'submit')
    NAME_RETURN = (By.ID, 'name')


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