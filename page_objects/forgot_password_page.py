from selenium.webdriver.remote.webdriver import WebDriver
from locators import ForgotPasswordPageLocators
from urls import FORGOT_PASSWORD_URL

class ForgotPasswordPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(FORGOT_PASSWORD_URL)

    def enter_email(self, email: str):
        email_input = self.driver.find_element(*ForgotPasswordPageLocators.email_input)
        email_input.clear()  # Очищаем поле перед вводом
        email_input.send_keys(email)

    def click_submit_reset_button(self):
        submit_button = self.driver.find_element(*ForgotPasswordPageLocators.submit_reset_button)
        submit_button.click()

    def click_toggle_password_button(self):
        toggle_button = self.driver.find_element(*ForgotPasswordPageLocators.email_field)
        toggle_button.click()

    def is_email_field_active(self) -> bool:
        # Проверка, что поле активно (подсвеченное)
        email_field = self.driver.find_element(*ForgotPasswordPageLocators.email_field)
        active_element = self.driver.switch_to.active_element
        return email_field == active_element

    def close_browser(self):
        self.driver.quit()