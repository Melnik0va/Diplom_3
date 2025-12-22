from selenium.webdriver.common.by import By

class RecoveryPasswordLocators: 
    FORGOT_PASSWORD_TITLE = [By.XPATH, "//h2[text()='Восстановление пароля']"]
    EMAIL_FIELD = [By.XPATH, ".//input[@name = 'name']"]
    BUTTON_RECOVERY = [By.XPATH, ".//button[text() = 'Восстановить']"]
    PASSWORD_FIELD = [By.XPATH, "//*[contains(@class, 'Auth_form')]/fieldset[1]/div/div"]
    ACTIVE_PASSWORD_FIELD = [By.XPATH, "//*[contains(@class , 'input_type_password')]"]
    EYE_ICON = [By.XPATH, "//*[contains(@class , 'input_type_password')]"]

    

