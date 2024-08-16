from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    SUBMIT_RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    TOGGLE_PASSWORD_BUTTON = (By.XPATH, "//input[@type='password' and @name='Введите новый пароль']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")


class PersonalAccountLocators:
    PROFILE_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class ConstructorLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    BUN_FLUORESCENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    SAUCE_SPICY_X = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    BUN_FLUORESCENT_TOP = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]")
    SAUCE_SPICY_X_TOP = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")
    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]//button[contains(@class,'Modal_modal__close_modified')]")
    ORDER_ID = (By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")
    CLOSE_BUTTON_ORDER = (By.CSS_SELECTOR, "section[class^='Modal_modal_opened'] button")
    ORDER_MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//p[contains(text(),'Дождитесь готовности на орбитальной станции')]")
    LAST_ORDER_IN_HISTORY = (By.XPATH, "(//a[contains(@class, 'OrderHistory_link__1iNby')])[last()]")



class OrderFeedLocators:
    ORDERS_FEED_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a/p")
    COMPLETED_COUNT = (By.CSS_SELECTOR, "selector-for-completed-count")
    TODAY_COMPLETED_COUNT = (By.CSS_SELECTOR, "selector-for-today-completed-count")
    ORDER_MODAL = (By.XPATH, "//*[@id='root']/div/section[2]/div[1]/div")
    ORDER_ELEMENT = (By.XPATH, "//*[@id='root']/div/main/div/div/ul/li[1]/a")
    CLOSE_BUTTON_SVG = (By.XPATH, "//*[@id='root']/div/section[2]/div[1]/button")
