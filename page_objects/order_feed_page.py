from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderFeedLocators

class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Методы для взаимодействия с элементами страницы
    def open_orders_feed(self):
        self.wait.until(EC.element_to_be_clickable(OrderFeedLocators.ORDERS_FEED_BUTTON)).click()

    def get_completed_count(self):
        return int(self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.COMPLETED_COUNT)).text)

    def get_today_completed_count(self):
        return int(self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.TODAY_COMPLETED_COUNT)).text)

    def open_order_details(self):
        self.wait.until(EC.element_to_be_clickable(OrderFeedLocators.ORDER_ELEMENT)).click()

    def is_order_modal_open(self):
        return self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.ORDER_MODAL)).is_displayed()

    def close_order_modal(self):
        close_button = self.wait.until(EC.element_to_be_clickable(OrderFeedLocators.CLOSE_BUTTON_SVG))
        close_button.click()
        # Подождите некоторое время, чтобы убедиться, что модальное окно закрывается
        self.wait.until(EC.invisibility_of_element_located(OrderFeedLocators.ORDER_MODAL))