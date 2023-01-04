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
    IPHONE_CHECKBOX = (By.XPATH, "/html/body/div[10]/div[2]/aside/div[1]/div[3]/div[3]/div[2]/label[1]/small")
    RAM_4_GB = (By.XPATH, '/html/body/div[10]/div[2]/aside/div[1]/div[3]/div[14]/div[2]/label[2]/small')
    SHOW_BUTTON = (By.XPATH, "/html/body/div[10]/div[2]/aside/script/text()")
    MOBILE_PHONES = (By.LINK_TEXT, "Мобильные телефоны")

    """GETTERS"""

    def get_price_slider_from(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.PRICE_SLIDER_FROM))

    def get_price_slider_to(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.PRICE_SLIDER_TO))

    def get_checkbox_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.IPHONE_CHECKBOX))

    def get_checkbox_ram_4_gb(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.RAM_4_GB))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.SHOW_BUTTON))

    """ACTIONS"""

    def click_price_slider_from(self):
        self.click_and_hold_slider(locator=self.get_price_slider_from(), x=110, y=0)
        print("COST OF ITEM SLIDER FROM")

    def click_price_slider_to(self):
        self.click_and_hold_slider(locator=self.get_price_slider_to(), x=-30, y=0)
        print("COST OF ITEM SLIDER TO")

    def select_checkbox_apple(self):
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        self.click_element_emulate_human(self.get_checkbox_apple())
        print("APPLE CHECKBOX")

    def select_checkbox_4gb(self):
        self.driver.execute_script("window.scrollTo(0, 1800)")
        time.sleep(1)
        self.click_element_emulate_human(self.get_checkbox_ram_4_gb())
        print("RAM 4 GB CHECKBOX")

    def click_show_button(self):
        self.click_element_emulate_human(self.get_show_button())
        print("Click")

    """Create Executable Function"""
    def get_filter_and_add_to_cart(self):
        time.sleep(1)
        self.select_checkbox_apple()
        time.sleep(4)
        self.select_checkbox_4gb()
        time.sleep(4)
        self.click_price_slider_from()
        time.sleep(4)
        self.click_price_slider_to()
        time.sleep(4)
        self.click_show_button()
        # self.select_checkbox_apple()
        time.sleep(5)

