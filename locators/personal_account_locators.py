from selenium.webdriver.common.by import By

class PersonalAccountLocators(): 
    TITTLE_LOGIN = [By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9" and contains(text(), "Профиль")]']
    EMAIL_FIELD = [By.XPATH, ".//input[@name = 'name']"]
    PASSWORD_FIELD = [By.XPATH, "//input[@name='Пароль']"]
    BUTTON_LOGIN = [By.XPATH,  "//button[contains(text(), 'Войти')]"]
    BUTTON_FORGOT_PASSWORD = [By.XPATH, "//a[text()='Восстановить пароль']"]

    BUTTON_HISTORY = [By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive' and contains(text(), 'История заказов')]"]
    BUTTON_EXIT = [By.XPATH,  "//button[contains(text(), 'Выход')]"]

    ORDER_NUMBER = [By.XPATH, "//*[contains(text(), '#')]"]

