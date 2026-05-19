import allure
import configuration
from pages.authorization_page import AuthorizationPage


class TestAuthorization:

    @allure.title('Авторизация')
    def test_authorization(self, driver_for_auth):
        driver, username, password = driver_for_auth
        authorization_page = AuthorizationPage(driver)
        authorization_page.input_authirization_form(username, password)
        logout_in_header = authorization_page.click_login_button()

        assert authorization_page.get_current_url() == configuration.URL + \
            configuration.MAIN_PAGE and logout_in_header.is_displayed()
