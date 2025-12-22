import allure 

from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage

class TestOrderFeedPage: 

    @allure.title('Открытие всплывающего окна с деталями заказа')
    def test_open_window_with_order_details(self, driver): 
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        order_number = order_feed_page.get_order_number(0)
        order_feed_page.click_order_number(0)

        assert order_feed_page.get_order_number_witn_opened_window() == order_number

    @allure.title('Заказы пользователя из раздела"История заказов" отображаются на странице "Лента заказов"')
    def test_orders_user_in_order_feed_page(self, driver, login_user): 
        main_page = MainPage(driver)
        main_page.create_order()

        account_page = PersonalAccountPage(driver)
        account_page.open_account_url()
        account_page.click_to_histrory_orders()
        user_orders = account_page.get_order_number()


        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()

        assert order_feed_page.get_all_orders(user_orders)

    @allure.title('При создании нового заказа счетчик "Выполнено за все время" увеличивается')
    def test_order_counter_all_the_time(self, driver, login_user): 
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        
        order_feed_page = OrderFeedPage(driver)
        counter_one = order_feed_page.get_counter_all_time()

        main_page.click_constructor_button()
        main_page.create_order()
        order_feed_page.open_order_feed_page()
        counter_two = order_feed_page.get_counter_all_time()

        assert counter_two > counter_one

    @allure.title('При создании нового заказа счетчик "Выполнено за сегодня" увеличивается')
    def test_order_counter_today(self, driver, login_user): 
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        
        order_feed_page = OrderFeedPage(driver)
        counter_one = order_feed_page.get_counter_today()

        main_page.click_constructor_button()
        main_page.create_order()
        order_feed_page.open_order_feed_page()
        counter_two = order_feed_page.get_counter_today()

        assert counter_two > counter_one

    @allure.title('После оформления заказа его номер отображается в разделе "В работе"')
    def test_order_in_work(self, driver, login_user): 
        main_page = MainPage(driver)
        main_page.add_ingredient_to_cart(0)
        main_page.add_ingredient_to_cart(2)
        main_page.add_ingredient_to_cart(3)
        main_page.click_on_order_button()
        main_page.wait_loading_create_order()
        order_number = main_page.get_order_number_in_opened_window()
        main_page.click_on_close_button_opened_window()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        
        assert order_number in order_feed_page.get_order_number_in_work()

