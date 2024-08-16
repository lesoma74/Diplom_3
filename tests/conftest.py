import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from urls import FORGOT_PASSWORD_URL, LOGIN_URL, BASE_URL



@pytest.fixture(scope="function", params=["chrome", "firefox"])
def browser(request):
    return request.param


@pytest.fixture(scope="function")
def driver(browser):
    if browser == "chrome":
        chrome_options = ChromeOptions()

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
    else:
        raise ValueError(f"Browser {browser} not supported")

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def open_home_page(driver):
    driver.get(BASE_URL)


@pytest.fixture(scope="function")
def open_login_page(driver):
    driver.get(LOGIN_URL)


@pytest.fixture(scope="function")
def open_forgot_password_page(driver):
    driver.get(FORGOT_PASSWORD_URL)







