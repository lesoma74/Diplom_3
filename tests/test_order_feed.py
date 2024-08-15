import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.order_feed_page import OrderFeedPage
from page_objects.profile_page import LoginPage, ProfilePage
from page_objects.constructor_page import ConstructorPage
from data import TestData
from urls import PROFILE_URL, CONSTRUCTOR_URL, FEED_URL
from locators import ConstructorLocators
import time


@pytest.mark.usefixtures("driver", "open_login_page")
class TestOrderFeed:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.order_feed_page = OrderFeedPage(driver)
        self.constructor_page = ConstructorPage(driver)
        self.wait = WebDriverWait(driver, 10)
        self.email = TestData.REGISTERED_EMAIL
        self.password = TestData.REGISTERED_PASSWORD

    @allure.title("Проверка открытия и закрытия модального окна деталей заказа")
    @allure.description(
        "Тест проверяет открытие и закрытие модального окна деталей заказа после оформления заказа и перехода в ленту заказов.")
    def test_order_details_modal_opens_and_closes(self, driver):
        # Логин
        self.login_page.login(self.email, self.password)

        # Переход в конструктор
        constructor_button = self.wait.until(EC.element_to_be_clickable(ConstructorLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()
        self.wait.until(EC.url_contains(CONSTRUCTOR_URL))

        # Добавить ингредиенты
        # Перетащить булку в зону заказа
        self.constructor_page.drag_and_drop_ingredient(
            ConstructorLocators.BUN_FLUORESCENT,
            ConstructorLocators.BUN_FLUORESCENT_TOP
        )

        # Перетащить соус в зону заказа
        self.constructor_page.drag_and_drop_ingredient(
            ConstructorLocators.SAUCE_SPICY_X,
            ConstructorLocators.SAUCE_SPICY_X_TOP
        )

        # Оформить заказ
        self.constructor_page.place_order()

        # Закрыть модальное окно заказа
        self.constructor_page.close_order_modal()

        # Ожидание, пока модальное окно исчезнет
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")))

        # Переход в личный кабинет
        self.profile_page.click_profile_button()
        self.wait.until(EC.url_contains(PROFILE_URL))
        assert PROFILE_URL in driver.current_url

        # Нажать на кнопку "История заказов"
        self.profile_page.click_order_history()

        # Прокрутка до последнего элемента в истории заказов
        last_order = self.wait.until(EC.presence_of_element_located(ConstructorLocators.LAST_ORDER_IN_HISTORY))
        driver.execute_script("arguments[0].scrollIntoView(true);", last_order)

        # Проверка того, что последний элемент действительно последний
        assert last_order.is_displayed()

        # Переход в ленту заказов
        orders_feed_button = self.wait.until(EC.element_to_be_clickable(ConstructorLocators.ORDERS_FEED_BUTTON))
        orders_feed_button.click()
        self.wait.until(EC.url_contains(FEED_URL))

        # Открыть ленту заказов
        self.order_feed_page.open_orders_feed()

        # Открыть детали заказа
        self.order_feed_page.open_order_details()

        # Проверка, что модальное окно с деталями заказа открылось
        assert self.order_feed_page.is_order_modal_open()

        # Закрытие модального окна
        self.order_feed_page.close_order_modal()

        # Задержка на странице ленты заказов после закрытия модального окна
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/div/div/div[2]/p[1]")))

        # Дополнительное ожидание для стабильности теста, если необходимо
        time.sleep(2)

