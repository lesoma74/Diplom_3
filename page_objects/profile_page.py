from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PersonalAccountLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_email(self, email):
        email_input = self.wait.until(EC.presence_of_element_located(PersonalAccountLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(EC.presence_of_element_located(PersonalAccountLocators.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.get_login_button()
        self.wait.until(EC.element_to_be_clickable(login_button))
        login_button.click()

    def get_login_button(self):
        return self.driver.find_element(*PersonalAccountLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_profile_button(self):
        profile_button = self.wait.until(EC.element_to_be_clickable(PersonalAccountLocators.PROFILE_BUTTON))
        profile_button.click()

    def click_order_history(self):
        order_history_link = self.wait.until(EC.element_to_be_clickable(PersonalAccountLocators.ORDER_HISTORY_LINK))
        order_history_link.click()

    def click_logout_button(self):
        logout_button = self.wait.until(EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON))
        logout_button.click()



