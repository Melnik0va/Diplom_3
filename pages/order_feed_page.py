import allure 

from data import URLS
from locators.order_feed_locators import OrderFeedLOcators
from pages.base_page import BasePage

class OrderFeedPage(BasePage): 
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переходим на страницу "Лента заказов"')
    def open_order_feed_page(self): 
        self.open_url(URLS.ORDER_FEED_URL)

    @allure.step('Получаем номер заказа')
    def get_order_number(self, number): 
        order_number = self.get_visible_elements(OrderFeedLOcators.NUMBER_ORDER)
        return order_number[number].text

    @allure.step('Нажимаем на заказ по его номеру')
    def click_order_number(self, number): 
        order_number = self.get_visible_elements(OrderFeedLOcators.LIST_ORDERS)
        order_number[number].click()

    @allure.step('Получаем номер заказа с открывшегося окна')
    def get_order_number_witn_opened_window(self): 
        return self.get_visible_element(OrderFeedLOcators.ORDER_NUMBER_WITH_OPENED_WINDOW).text
    
    @allure.step('Получаем список с номерами заказов')
    def get_orders_number(self): 
        orders_numbers = list(order_number.text for order_number in self.get_visible_elements(
            OrderFeedLOcators.ORDERS_NUMBER_LIST))
        return orders_numbers

    @allure.step('Проверяем наличие заказов')
    def get_all_orders(self, user_orders):
        feed_orders = self.get_orders_number()
        return all(order_number in feed_orders for order_number in user_orders)
    
    @allure.step('Получаем число заказов из раздела "Выполнено за все время"')
    def get_counter_all_time(self): 
        return int(self.get_visible_element(OrderFeedLOcators.COUNTER_ALL_TIME).text)
    
    @allure.step('Получаем число зазкаов из раздела "Выполнено за сегодня"')
    def get_counter_today(self): 
        return int(self.get_visible_element(OrderFeedLOcators.COUNTER_TODAY).text)
    
    @allure.step('Получаем номер заказа из раздела "В работе"')
    def get_order_number_in_work(self): 
        return list(order_number.text for order_number in self.get_visible_elements(OrderFeedLOcators.ORDERS_NUMBER_LIST_IN_WORK))
    