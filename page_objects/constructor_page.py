from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import ConstructorLocators
from selenium.webdriver.common.keys import Keys
import time


class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.action = ActionChains(driver)


    def drag_and_drop_ingredient(self, ingredient_locator, target_locator):
        ingredient = self.wait.until(EC.visibility_of_element_located(ingredient_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        self.action.drag_and_drop(ingredient, target).perform()

    def place_order(self):
        order_button = self.wait.until(EC.element_to_be_clickable(ConstructorLocators.ORDER_BUTTON))
        order_button.click()

    def close_order_modal(self):

        time.sleep(2)  # Задержка на 2 секунды

        body_element = self.driver.find_element(By.TAG_NAME, "body")
        body_element.send_keys(Keys.ESCAPE)
