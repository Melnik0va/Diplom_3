import allure
import pytest

from data import URLS
from pages.main_page import MainPage

class TestMainPage: 

    @allure.title('Переход по клику на "Конструктор"')
    def test_click_on_constructor_button(self, driver): 
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed_button()
        main_page.click_constructor_button()

        assert main_page.current_url == URLS.BASE_URL

    @allure.title('Переход по клику на "Лента заказов"')
    def test_click_on_order_feed_button(self, driver): 
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed_button()

        assert main_page.current_url == URLS.ORDER_FEED_URL

    @allure.title('Открытие всплывающего окна с деталями ингредиента по клику')
    def test_show_details_ingredient(self, driver): 
        main_page = MainPage(driver)
        main_page.open_main_page()
        name = main_page.get_name_ingredient_by_number(0)
        main_page.click_on_ingredient(0)

        assert main_page.get_name_ingredient_with_open_window() == name

    @allure.title('Закрытие всплывающего окна с деталями ингредиента')
    def test_close_opened_ingredient_details(self, driver): 
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient(0)
        main_page.click_on_close_button_opened_window()

        assert main_page.check_invisible_window_with_details()

    @allure.title('Увеличение каунтера ингредиента при его добавлении в заказ')
    @pytest.mark.parametrize('ingredient_number, counter_amount', [(1, 2), (3, 1)])
    def test_ingredient_counter(self, driver, ingredient_number, counter_amount): 
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_one = main_page.get_counter_ingredient(ingredient_number)
        main_page.add_ingredient_to_cart(ingredient_number)
        counter_two = main_page.get_counter_ingredient(ingredient_number)

        assert counter_two == counter_one + counter_amount

    @allure.title('Оформление заказа залогиненным пользователем')
    def test_create_order_user_authorization(self, driver, login_user): 
        main_page = MainPage(driver)
        main_page.add_ingredient_to_cart(0)
        main_page.add_ingredient_to_cart(2)
        main_page.add_ingredient_to_cart(3)
        main_page.click_on_order_button()

        assert main_page.check_order_status() == 'Ваш заказ начали готовить'


