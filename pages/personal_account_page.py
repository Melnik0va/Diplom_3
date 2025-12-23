import allure

from data import URLS
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators

class PersonalAccountPage(BasePage): 
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу авторизации')
    def open_login_url(self): 
        self.open_url(URLS.LOGIN_URL)

    @allure.step('Открываем страницу аккаунта пользователя')
    def open_account_url(self): 
        self.open_url(URLS.ACCOUNT_URL)

    @allure.step('Кликаем по кнопке "Восстановить пароль"')
    def click_button_forgot_password(self): 
        self.click_to_element(PersonalAccountLocators.BUTTON_FORGOT_PASSWORD)

    @allure.step('Ждем полную загрузку страницы авторизации')
    def wait_to_autoform(self): 
        self.find_element_with_wait(PersonalAccountLocators.TITTLE_LOGIN)

    @allure.step('Заполняем поле "email"')
    def fill_field_email(self, email): 
        self.add_text_to_element(PersonalAccountLocators.EMAIL_FIELD, email)

    @allure.step('Заполняем поле "пароль"')
    def fill_field_password(self, password):
        self.add_text_to_element(PersonalAccountLocators.PASSWORD_FIELD, password)

    @allure.step('Кликаем по кнопке "Войти"')
    def click_to_login_button(self): 
        self.click_to_element(PersonalAccountLocators.BUTTON_LOGIN)

    @allure.step('Заполняем форму авторизации')
    def authorization_user(self, email, password): 
        self.fill_field_email(email)
        self.fill_field_password(password)
        self.click_to_login_button()

    @allure.step('Кликаем по кнопке "История заказов"')
    def click_to_histrory_orders(self): 
        self.click_to_element(PersonalAccountLocators.BUTTON_HISTORY)

    @allure.step('Кликаем по кнопке "Выход"')
    def click_exit_button(self): 
        self.click_to_element(PersonalAccountLocators.BUTTON_EXIT)
        
    @allure.step('Дожидаемся загрузки страницы авторизации')
    def wait_login_user(self):
        self.find_element_with_wait(PersonalAccountLocators.BUTTON_LOGIN) 

    @allure.step('Получаем номер заказа пользователя из раздела "История заказов"')
    def get_order_number(self): 
        order_number = list(order_number.text for order_number in self.get_visible_elements(
            PersonalAccountLocators.ORDER_NUMBER))
        return order_number