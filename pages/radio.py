from selenium.webdriver.common.by import By

class Radio:

    URL = "https://demoqa.com/radio-button"
    YES_RADIO = (By.ID, 'yesRadio')
    IMPRESSIVE_RADIO = (By.ID, 'impressiveRadio')
    NO_RADIO = (By.ID, 'noRadio')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_no(self):
        no_radio = self.browser.find_element(*self.NO_RADIO)
        if no_radio.is_enabled():
            return True
        else:
            return False

    # is there a way to refactor this and other following methods to work for both yes and impressive?
    def check_yes(self):
        yes_radio = self.browser.find_element(*self.YES_RADIO)
        if yes_radio.is_enabled():
            return True
        else:
            return False

    def check_impressive(self):
        impressive_radio = self.browser.find_element(*self.IMPRESSIVE_RADIO)
        if impressive_radio.is_enabled():
            return True
        else:
            return False

    def select_yes(self):
        self.browser.find_element(*self.YES_RADIO).click()