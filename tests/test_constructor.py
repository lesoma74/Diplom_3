import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.profile_page import LoginPage, ProfilePage
from page_objects.constructor_page import ConstructorPage
from data import TestData
from urls import LOGIN_URL, HOME_URL, CONSTRUCTOR_URL, FEED_URL
from locators import ConstructorLocators

@pytest.mark.usefixtures("driver", "open_login_page")
class TestConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.constructor_page = ConstructorPage(driver)
        self.wait = WebDriverWait(driver, 20)
        self.action = ActionChains(driver)
        self.email = TestData.REGISTERED_EMAIL
        self.password = TestData.REGISTERED_PASSWORD

    @allure.title("Тестирование перехода в ленту заказов и конструктора")
    @allure.description(
        "Проверка перехода в ленту заказов и конструктора, включая добавление ингредиентов и оформление заказа.")
    def test_order_feed_and_constructor(self, driver):
        # Шаг 1-4: Вход на главную страницу
        driver.get(LOGIN_URL)
        self.login_page.enter_email(self.email)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()
        self.wait.until(EC.url_contains(HOME_URL))

        # Шаг 5: Перейти на ленту заказов
        orders_feed_button = self.wait.until(EC.element_to_be_clickable(ConstructorLocators.orders_feed_button))
        orders_feed_button.click()
        self.wait.until(EC.url_contains(FEED_URL))

        # Шаг 6: Проверка уникального элемента на странице ленты заказов
        unique_element_locator = (By.XPATH, "//h1[text()='Лента заказов']")
        self.wait.until(EC.visibility_of_element_located(unique_element_locator))

        # Шаг 7: Вернуться на главную через конструктор
        constructor_button = self.wait.until(EC.element_to_be_clickable(ConstructorLocators.constructor_button))
        constructor_button.click()
        self.wait.until(EC.url_contains(CONSTRUCTOR_URL))

        # Шаг 8: Нажать на булку, чтобы открыть модальное окно
        bun_element = self.wait.until(EC.element_to_be_clickable(ConstructorLocators.bun_fluorescent))
        bun_element.click()

        # Шаг 9: Закрыть модальное окно
        close_button = self.wait.until(EC.element_to_be_clickable(ConstructorLocators.close_button))
        close_button.click()

        # Шаг 10: Добавить ингредиенты
        self.constructor_page.drag_and_drop_ingredient(
            ConstructorLocators.bun_fluorescent,
            ConstructorLocators.bun_fluorescent_top
        )
        self.constructor_page.drag_and_drop_ingredient(
            ConstructorLocators.sauce_spicy_x,
            ConstructorLocators.sauce_spicy_x_top
        )

        # Шаг 11: Оформить заказ
        self.constructor_page.place_order()

        # Шаг 13: Закрыть модальное окно
        self.constructor_page.close_order_modal()