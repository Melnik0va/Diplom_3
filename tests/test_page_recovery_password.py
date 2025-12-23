import allure

from data import URLS
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_password_page import RecoveryPasswordPage

class TestRecoveryPassword: 

    @allure.title('Переход на страницу восстановления паароля по кнопку "Восстановить пароль"')
    def test_open_recovery_password_page(self, driver): 
        login_page = PersonalAccountPage(driver)
        login_page.open_login_url()
        login_page.click_button_forgot_password() 

        assert login_page.current_url == URLS.FORGOT_PASSWORD

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_recovery_password_with_email(self, driver, create_user): 
        login_page = PersonalAccountPage(driver)
        login_page.open_login_url()
        login_page.click_button_forgot_password() 
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.fill_field_email(create_user['email'])
        recovery_page.click_to_recovery_button()
        recovery_page.wait_loading_page()

        assert recovery_page.current_url == URLS.RESET_URL

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным - подсвечивает его')
    def test_click_eye_button_and_show_password(self, driver, create_user): 
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_recovery_password_page()
        recovery_page.fill_field_email(create_user['email'])
        recovery_page.click_to_recovery_button()
        class_active = recovery_page.get_active_password_field()
        recovery_page.click_icon_eye_icopn()
        
        assert 'input_status_active' in class_active.get_attribute('class')
