import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Collection of actions"""
    def hover_on_element_emulate_human(self, locator):
        ActionChains(self.driver).pause(0.3).move_to_element(locator).perform()

    def click_element_emulate_human(self, locator):
        ActionChains(self.driver).pause(0.3).move_to_element(locator).click().perform()

    def scroll_to_element_and_click(self, locator):
        ActionChains(self.driver).pause(0.3).scroll_to_element(locator).click().perform()

    def click_and_send_value(self, locator, value):
        ActionChains(self.driver).pause(0.3).move_to_element(locator).click().send_keys(value).perform()

    def verify_element_to_be_clickable(self, locator: tuple):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    def verify_element_to_be_visible(self, locator: tuple):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator: tuple):
        return self.verify_element_to_be_clickable(locator)

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"CURRENT URL: {get_url}")

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"GOOD VALUE WORLD: {value_word} CORRESPOND {result}")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"GOOD VALUE URL {get_url}")

    def get_param_url(self, param: str):
        self.driver.get(self.driver.current_url + param)

    """Method screen shot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'SCREENSHOT ' + now_date + '.png'
        self.driver.save_screenshot('/Users/alexanderlevkin/Desktop/LESSONS/Onliner/SCREEN/' + name_screenshot)
