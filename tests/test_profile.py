import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.profile_page import LoginPage, ProfilePage
from data import TestData
from urls import LOGIN_URL, BASE_URL, PROFILE_URL

@pytest.mark.usefixtures("driver", "open_login_page")
class TestEntranceLogoutFromProfile:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.wait = WebDriverWait(driver, 20)
        self.email = TestData.REGISTERED_EMAIL
        self.password = TestData.REGISTERED_PASSWORD

    @allure.title("Тест: Выход из профиля")
    @allure.description(
        "Тест выполняет вход на сайт, переходит на страницу профиля, выходит из системы и проверяет переход на страницу входа.")
    def test_entrance_logout_from_profile(self, driver):
        # Шаг 1: Открыть страницу входа
        driver.get(LOGIN_URL)

        # Шаг 2: Ввести email и пароль для входа
        self.login_page.enter_email(self.email)
        self.login_page.enter_password(self.password)

        # Шаг 3: Нажать на кнопку "Войти"
        self.login_page.click_login_button()

        # Шаг 4: Проверка URL после успешного входа (на главной странице)
        self.wait.until(EC.url_contains(BASE_URL))
        assert BASE_URL in driver.current_url

        # Шаг 5: Нажать на кнопку "Личный кабинет"
        self.profile_page.click_profile_button()

        # Шаг 6: Проверка URL после перехода на страницу профиля
        self.wait.until(EC.url_contains(PROFILE_URL))
        assert PROFILE_URL in driver.current_url

        # Шаг 7: Нажать на кнопку "История заказов"
        self.profile_page.click_order_history()

        # Шаг 8: Нажать на кнопку "Выход"
        self.profile_page.click_logout_button()

        # Шаг 9: Проверка URL после выхода (на странице входа)
        self.wait.until(EC.url_contains(LOGIN_URL))
        assert LOGIN_URL in driver.current_url












