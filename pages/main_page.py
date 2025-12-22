import allure

from data import URLS
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage): 
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = URLS.BASE_URL

    @allure.step('Открываем главную страницу')
    def open_main_page(self): 
        self.open_url(MainPageLocators.LOADING_ANIMATION, URLS.BASE_URL)

    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_account_button(self): 
        self.click_to_element(MainPageLocators.LOADING_ANIMATION, MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_order_feed_button(self): 
        self.click_to_element(MainPageLocators.LOADING_ANIMATION, MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_constructor_button(self): 
        self.click_to_element(MainPageLocators.LOADING_ANIMATION, MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получаем название ингредиента по выбранному номеру')
    def get_name_ingredient_by_number(self, number): 
        ingredient = self.get_visible_elements(MainPageLocators.LIST_BUN_INGREDIENTS)
        return ingredient[number].text.split('\n')[2]
    
    @allure.step('Нажимаем на ингредиент повыбранному номеру')
    def click_on_ingredient(self, number): 
        ingredient = self.get_visible_elements(MainPageLocators.LIST_BUN_INGREDIENTS)
        ingredient[number].click()

    @allure.step('Получаем название ингредиента с открывшегося окня')
    def get_name_ingredient_with_open_window(self): 
        return self.get_visible_element(MainPageLocators.INGREDIENT_NAME_WITH_OPEN_WINDOW).text
    
    @allure.step('Закрываем окно с деталями')
    def click_on_close_button_opened_window(self): 
        self.click_to_element(MainPageLocators.LOADING_ANIMATION, MainPageLocators.CLOSE_OPENED_WINDOW_INGREDIENT_DETAILS)

    @allure.step('Проверка невидимости эелемента')
    def check_invisible_window_with_details(self): 
        return self.check_invisible_element(MainPageLocators.TITTLE_INGREDIENT_DETAILS)
    
    @allure.step('Получаем количество ингредиментов')
    def get_counter_ingredient(self, number): 
        counter = self.get_visible_elements(MainPageLocators.COUNTER_INGREDIENT)
        return int(counter[number].text)
    
    @allure.step('Добавляем ингредиенты в корзину(заказ)')
    def add_ingredient_to_cart(self, number): 
        ingredient = self.get_visible_elements(MainPageLocators.LIST_BUN_INGREDIENTS)
        cart = self.get_visible_element(MainPageLocators.CART_WITN_INGREDIENTS)
        self.drag_and_drop(ingredient[number], cart)

    @allure.step('Нажиаем на кнопку "Оформить"')
    def click_on_order_button(self): 
        self.click_to_element(MainPageLocators.LOADING_ANIMATION, MainPageLocators.ORDER_BUTTON)

    @allure.step('Получаем статус заказа')
    def check_order_status(self): 
        return self.get_visible_element(MainPageLocators.ORDER_STATUS).text
    
    @allure.step('Ждем загрузку заказа')
    def wait_loading_create_order(self): 
        self.wait_loading(MainPageLocators.LOADING_ANIMATION)

    @allure.step('Создаем заказ')
    def create_order(self): 
        self.add_ingredient_to_cart(0)
        self.add_ingredient_to_cart(2)
        self.add_ingredient_to_cart(3)
        self.click_on_order_button()
        self.wait_loading_create_order()
        self.click_on_close_button_opened_window()

    @allure.step('Получаем номер заказа с открывшегося окна при его оформлении')
    def get_order_number_in_opened_window(self): 
        return f'0{self.find_element_with_wait
                   (MainPageLocators.TITTLE_ORDER_NUMBER_IN_OPENED_WINDOW).text}'
