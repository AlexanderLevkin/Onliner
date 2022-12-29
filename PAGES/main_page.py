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
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    ENTER_BUTTON = (By.XPATH, '//input[@value="Войти"]')
    LOGIN = "alexanlevkin@gmail.com"
    PASSWORD = "TestSelenium"

    """GETTERS"""

    def get_authorization_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.AUTHORIZATION_BUTTON))

    def get_login_field(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.EMAIL_FIELD))

    def get_password_field(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.PASSWORD_FIELD))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.ENTER_BUTTON))

    """ACTIONS"""

    def click_authorization_button(self):
        self.click_element_emulate_human(self.get_authorization_button())
        print("CLICK ON THE ENTER BUTTON")

    def click_login_field(self):
        self.click_and_send_value(self.get_login_field(), self.LOGIN)
        print("FILL IN THE LOGIN")

    def click_password_field(self):
        self.click_and_send_value(self.get_password_field(), self.PASSWORD)
        print("FILL IN THE LOGIN")

    def click_enter_button(self):
        self.click_element_emulate_human(self.get_enter_button())
        print("ENTER TO THE ACCOUNT")

    # Methods

    def enter_to_account(self):
        self.get_current_url()
        self.click_authorization_button()
        self.click_login_field()
        self.click_password_field()
        self.click_enter_button()
        time.sleep(3)
        self.get_screenshot()
