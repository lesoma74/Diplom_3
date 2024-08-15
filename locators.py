from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:

  profile_button = (By.XPATH, "//p[text()='Личный Кабинет']")
  reset_password_button = (By.XPATH, "//a[text()='Восстановить пароль']")
  email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")
  submit_reset_button = (By.XPATH, "//button[text()='Восстановить']")
  toggle_password_button = (By.XPATH, "//input[@type='password' and @name='Введите новый пароль']")
  email_field = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
  order_history_link = (By.XPATH, "//a[@href='/account/order-history']")


class PersonalAccountLocators:

  profile_button = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")
  email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")
  password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
  login_button = (By.XPATH, "//button[text()='Войти']")
  order_history_link = (By.XPATH, "//a[@href='/account/order-history']")
  logout_button = (By.XPATH, "//button[text()='Выход']")

class ConstructorLocators:
  constructor_button = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")
  orders_feed_button = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a/p")
  bun_fluorescent = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
  sauce_spicy_x = (By.XPATH, "//img[@alt='Соус Spicy-X']")
  ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
  bun_fluorescent_top = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]")
  sauce_spicy_x_top = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")
  close_button = (
  By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button[contains(@class,'Modal_modal__close_modified')]")
  order_id = (By.XPATH, "//*[@id='root']/div/section/div[1]/div")
  close_button_order = (By.XPATH, "//*[@id='root']/div/section/div[1]/button")
  order_modal = (By.XPATH, "//*[@id='root']/div/section/div[1]/div")
  LAST_ORDER_IN_HISTORY = (By.XPATH, "//*[@id='root']/div/main/div/div/div/ul/li[6]/a")


class OrderFeedLocators:
  orders_feed_button = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a/p")
  completed_count = (By.CSS_SELECTOR, "selector-for-completed-count")
  today_completed_count = (By.CSS_SELECTOR, "selector-for-today-completed-count")
  order_modal = (By.XPATH, "//*[@id='root']/div/section[2]/div[1]/div")
  order_element = (By.XPATH, "//*[@id='root']/div/main/div/div/ul/li[1]/a")
  close_button_svg = (By.XPATH, "//*[@id='root']/div/section[2]/div[1]/button")

