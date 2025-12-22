import allure

from data import URLS
from pages.base_page import BasePage
from locators.recovery_password_locators import RecoveryPasswordLocators

class RecoveryPasswordPage(BasePage): 
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу Восстановления пароля')
    def open_recovery_password_page(self): 
        self.open_url(URLS.FORGOT_PASSWORD)

    @allure.step('Заполняем поле "email"')
    def fill_field_email(self, email): 
        self.add_text_to_element(RecoveryPasswordLocators.EMAIL_FIELD, email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_to_recovery_button(self): 
        self.click_to_element(RecoveryPasswordLocators.BUTTON_RECOVERY)

    @allure.step('Ждем загрузку страницы ввода пароля')
    def wait_loading_page(self): 
        self.find_element_with_wait(RecoveryPasswordLocators.EYE_ICON)

    @allure.step('Получаем состояние поля "Пароль"')
    def get_active_password_field(self): 
        return self.get_visible_element(RecoveryPasswordLocators.ACTIVE_PASSWORD_FIELD)

    @allure.step('Нажимаем на кнопку показа/скрытия пароля')
    def click_icon_eye_icopn(self): 
        self.click_to_element(RecoveryPasswordLocators.EYE_ICON)
