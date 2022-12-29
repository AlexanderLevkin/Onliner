from selenium.webdriver import ActionChains

from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class MainPage(Base):
    # Locators

    AUTHORIZATION_BUTTON = (By.XPATH, '//a[@href="https://www.amd.by/login/"]')
    EMAIL_FIELD = (By.XPATH, '//input[@placeholder="E-Mail:"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@label="Пароль"]')
    # USER_LOGGED_FROM_DROP_DOWN_MENU = (By.XPATH, '//*[@id="userToolsDropDown"]/div/span')
    # ACCOUNT_LOGGED_BUTTON = (By.XPATH, '//*[@id="header"]/div/div[5]/div/div[3]/div/div/div/button')
    LOGIN = "alexanlevkin@gmail.com"
    PASSWORD = "TestSelenium"

    """GETTERS"""

    def get_enter_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.AUTHORIZATION_BUTTON))

    def get_login_field(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.EMAIL_FIELD))

    """ACTIONS"""

    def click_enter_button(self):
        self.click_element_emulate_human(self.get_enter_button())
        print("CLICK ON THE ENTER BUTTON")

    def click_login_field(self):
        self.click_and_send_value(self.get_login_field(), "LOGIN")
        print("CLICK ON THE ENTER BUTTON")

    # Methods

    def enter_to_account(self):
        self.get_current_url()
        self.click_enter_button()
        time.sleep(3)
        self.get_screenshot()
