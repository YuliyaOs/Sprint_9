from pages.base_page import BasePage
from locators import authorization_page_locators
import configuration
import allure


class AuthorizationPage(BasePage):

    @allure.step('Кликаем на кнопку "Войти" в хэдере сайта')
    def click_login_in_header(self):
        self.click_to_element(authorization_page_locators.login_in_header)
        self.wait_url_contains(configuration.SIGNIN)

    @allure.step('Заполняем форму авторизации')
    def input_authirization_form(self, username, password):
        self.enter_data_in_field(
            authorization_page_locators.username_input, username)
        self.enter_data_in_field(
            authorization_page_locators.password_input, password)

    @allure.step('Кликаем на кнопку "Войти" формы авторизации')
    def click_login_button(self):
        self.click_to_element(authorization_page_locators.login_button)
        self.wait_url_contains(configuration.MAIN_PAGE)
        return self.find_element(authorization_page_locators.logout_in_header)
