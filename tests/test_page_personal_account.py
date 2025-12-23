import allure

from data import URLS
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage



class TestPagePersonalAccount: 

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_personal_account(self, driver, login_user): 

        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)
        main_page.click_account_button()
        account_page.wait_to_autoform()

        assert account_page.current_url == URLS.PROFILE_URL

    @allure.title('Переход в раздел "История заказов"')
    def test_history_order(self, driver, login_user): 
        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)
        main_page.click_account_button()
        account_page.click_to_histrory_orders()

        assert account_page.current_url == URLS.ORDERS_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout_account(self, driver, login_user): 
        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)
        main_page.click_account_button()
        account_page.click_exit_button()
        account_page.wait_login_user()

        assert account_page.current_url == URLS.LOGIN_URL

