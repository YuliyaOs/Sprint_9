import allure
import configuration
from pages.create_account_page import CreateAccountPage


class TestCreateAccount:

    @allure.title('Создание аккаунта')
    def test_create_account(self, driver, data_for_create_user):
        create_account_page = CreateAccountPage(driver)
        create_account_page.click_create_account_in_header()
        create_account_page.input_signup_form(*data_for_create_user)
        signin_button = create_account_page.click_create_account_button()

        assert create_account_page.get_current_url() == configuration.URL + \
            configuration.SIGNIN and signin_button.is_displayed()
