from selenium.common import NoSuchWindowException, TimeoutException
from selenium.webdriver import ActionChains

from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class FilterPage(Base):
    """LOCATORS"""

    PRICE_SLIDER_FROM = (By.XPATH, '//*[@id="scale-price"]/div[1]/div[1]/div')
    PRICE_SLIDER_TO = (By.XPATH, '//*[@id="scale-price"]/div[1]/div[2]')
    IPHONE_CHECKBOX = (By.XPATH, "/html/body/div[11]/div[2]/aside/div[1]/div[3]/div[3]/div[2]/label[1]/small")
    RAM_4_GB = (By.XPATH, '/html/body/div[11]/div[2]/aside/div[1]/div[3]/div[14]/div[2]/label[2]/small')
    SHOW_BUTTON = (By.XPATH, '//button[@class ="btn btn-primary"]')
    MOBILE_PHONES = (By.LINK_TEXT, "Мобильные телефоны")
    IPHONE_11_128 = (By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[3]/div[1]/div/div[3]/div[2]/div[2]/button')
    ADDED_IPHONE_11_128_WHITE = (By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[3]/div[1]/div/div[3]/div[2]/div[2]'
                                           '/button')
    CART_BUTTON = (By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[3]/div[1]/div/div[3]/div[2]/div[2]/button')

    """GETTERS"""

    def get_price_slider_from(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.PRICE_SLIDER_FROM))

    def get_price_slider_to(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.PRICE_SLIDER_TO))

    def get_checkbox_apple(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.IPHONE_CHECKBOX))

    def get_checkbox_ram_4_gb(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.RAM_4_GB))

    def get_show_button(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.SHOW_BUTTON))

    def get_iphone_11_128(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.IPHONE_11_128))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.CART_BUTTON))

    """ACTIONS"""

    def click_price_slider_from(self):
        self.click_and_hold_slider(locator=self.get_price_slider_from(), x=110, y=0)
        print("COST OF ITEM SLIDER FROM")

    def click_price_slider_to(self):
        self.click_and_hold_slider(locator=self.get_price_slider_to(), x=-30, y=0)
        print("COST OF ITEM SLIDER TO")

    def select_checkbox_apple(self):
        self.driver.execute_script("window.scrollTo(0, 200)")
        self.click_element_emulate_human(self.get_checkbox_apple())
        print("APPLE CHECKBOX")

    def select_checkbox_4gb(self):
        self.driver.execute_script("window.scrollTo(0, 1800)")
        self.click_element_emulate_human(self.get_checkbox_ram_4_gb())
        print("RAM 4 GB CHECKBOX")

    def choose_iphone_11_128(self):
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.click_element(self.get_iphone_11_128())
        print("SELECT TO IPHONE 11 WHITE 128GB")

    def click_to_cart_button(self):
        self.click_element_emulate_human(self.get_cart_button())
        print("CLICK TO CART")

    """Create Executable Function
    Select the Item and use filters"""
    def get_filter_and_add_to_cart(self):
        self.select_checkbox_apple()
        time.sleep(4)
        self.select_checkbox_4gb()
        time.sleep(4)
        self.click_price_slider_from()
        time.sleep(4)
        self.click_price_slider_to()
        time.sleep(2)
        try:
            self.choose_iphone_11_128()
        except NoSuchWindowException:
            print("Phone isn't in scope")
        except TimeoutException:
            print("Phone isn't in scope")
        self.click_to_cart_button()



