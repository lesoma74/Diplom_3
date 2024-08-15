from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderFeedLocators

class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Методы для взаимодействия с элементами страницы
    def open_orders_feed(self):
        self.wait.until(EC.element_to_be_clickable(OrderFeedLocators.orders_feed_button)).click()

    def get_completed_count(self):
        return int(self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.completed_count)).text)

    def get_today_completed_count(self):
        return int(self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.today_completed_count)).text)

    def open_order_details(self):
        self.wait.until(EC.element_to_be_clickable(OrderFeedLocators.order_element)).click()

    def is_order_modal_open(self):
        return self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.order_modal)).is_displayed()

    def close_order_modal(self):
        close_button = self.wait.until(EC.element_to_be_clickable(OrderFeedLocators.close_button_svg))
        close_button.click()
        # Подождите некоторое время, чтобы убедиться, что модальное окно закрывается
        self.wait.until(EC.invisibility_of_element_located(OrderFeedLocators.order_modal))