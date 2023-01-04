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
    CHECK_WORD = (By.XPATH, '//*[@id="content"]/h2[1]')
    MAIN_PAGE_LOGO = (By.XPATH, '//img[@alt="Онлайн гипермаркет "AMD.BY""]')
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

    def get_check_word_enter_to_acc(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.CHECK_WORD))

    def get_main_page_logo(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.MAIN_PAGE_LOGO))

    """ACTIONS"""

    def click_authorization_button(self):
        self.click_element_emulate_human(self.get_authorization_button())
        print("CLICK ON THE ENTER BUTTON")

    def click_login_field(self):
        self.click_and_send_value(self.get_login_field(), self.LOGIN)
        print("FILL IN THE LOGIN")

    def click_password_field(self):
        self.click_and_send_value(self.get_password_field(), self.PASSWORD)
        print("FILL IN THE PASSWORD")

    def click_enter_button(self):
        self.click_element_emulate_human(self.get_enter_button())
        print("ENTER TO THE ACCOUNT")

    def check_word_enter_to_acc(self):
        self.assert_word(self.get_check_word_enter_to_acc(), "Моя учетная запись")

    def check_url(self):
        self.assert_url('https://www.amd.by/index.php?route=account/account')

    def transfer_to_the_main_page(self):
        self.click_element_emulate_human(self.get_main_page_logo())
        print("TRANSFER TO THE MAIN PAGE")

    # Methods

    def enter_to_account(self):
        self.get_current_url()
        self.click_authorization_button()
        self.click_login_field()
        self.click_password_field()
        self.click_enter_button()
        self.check_word_enter_to_acc()
        self.check_url()
        self.driver.get("https://www.amd.by/")
        self.get_screenshot()
        time.sleep(3)
