import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.forgot_password_page import ForgotPasswordPage
from data import TestData
from urls import FORGOT_PASSWORD_URL

@pytest.mark.usefixtures("driver", "open_forgot_password_page")
class TestForgotPasswordPage:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.forgot_password_page = ForgotPasswordPage(driver)
        self.email = TestData.REGISTERED_EMAIL
        self.wait = WebDriverWait(driver, 20)

    @allure.title("Тестирование процесса восстановления пароля")
    @allure.description("Проверка восстановления пароля через ввод почты и активацию поля для нового пароля")
    def test_reset_password_flow(self, driver):
        # Шаг 1: Ввод почты
        self.forgot_password_page.enter_email(self.email)

        # Шаг 2: Клик по кнопке "Восстановить"
        self.forgot_password_page.click_submit_reset_button()

        # Шаг 3: Ожидание видимости поля
        email_field_locator = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
        email_field = self.wait.until(EC.visibility_of_element_located(email_field_locator))

        # Клик на поле
        email_field.click()

        # Шаг 4: Проверка, что поле активное
        assert self.forgot_password_page.is_email_field_active(), "Email field was not activated"

    def teardown_method(self):
        # Закрытие браузера
        self.forgot_password_page.close_browser()