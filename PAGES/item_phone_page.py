from selenium.webdriver import ActionChains

from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class ItemPage(Base):
    # Locators

    ELECTRONICS_SECTION = (By.XPATH, '//div[@class="item-category-view-pc main-cats category_id59"]')
    MOBILE_PHONES_AND_ACCESSORIES = (By.XPATH, '//*[@id="But-Section-69-Category-59"]/p')
    MOBILE_PHONES = (By.LINK_TEXT, "Мобильные телефоны")

    """GETTERS"""

    def get_electronics_section(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.ELECTRONICS_SECTION))

    def get_mobile_and_accessories_section(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.MOBILE_PHONES_AND_ACCESSORIES))

    def get_mobile_section(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.MOBILE_PHONES))

    """ACTIONS"""

    def click_electronics_section(self):
        self.click_element_emulate_human(self.get_electronics_section())
        print("CLICK ON THE ELECTRONIC SECTION")

    def click_mobile_and_accessories_section(self):
        self.click_element_emulate_human(self.get_mobile_and_accessories_section())
        print("CLICK ON THE MOBILE AND ACCESSORIES SECTION")

    def click_mobile_section(self):
        self.click_element_emulate_human(self.get_mobile_section())
        print("CLICK ON THE MOBILE SECTION")

    def get_item(self):
        self.click_electronics_section()
        self.click_mobile_and_accessories_section()
        self.click_mobile_section()
        self.click_mobile_section()
        time.sleep(1)
        self.assert_url(result="https://www.amd.by/mobile/")
        time.sleep(3)
        # self.get_screenshot()
