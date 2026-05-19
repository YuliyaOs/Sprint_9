from pages.base_page import BasePage
from locators import create_account_page_locators
import configuration

import allure


class CreateAccountPage(BasePage):

    @allure.step('Кликаем на кнопку "Создать аккаунт" в хэдере сайта')
    def click_create_account_in_header(self):
        self.click_to_element(
            create_account_page_locators.create_account_in_header)
        self.wait_url_contains(configuration.CREATE_ACCOUNT)

    @allure.step('Кликаем на кнопку "Создать аккаунт" в форме создания аккаунта')
    def click_create_account_button(self):
        self.click_to_element(
            create_account_page_locators.create_account_button)
        self.wait_url_contains(configuration.SIGNIN)
        return self.find_element(create_account_page_locators.signin_button)

    @allure.step('Заполняем форму создания аккаунта')
    def input_signup_form(self, first_name, last_name, username, email, password):
        self.enter_data_in_field(
            create_account_page_locators.first_name_input, first_name)
        self.enter_data_in_field(
            create_account_page_locators.last_name_input, last_name)
        self.enter_data_in_field(
            create_account_page_locators.username_input, username)
        self.enter_data_in_field(
            create_account_page_locators.email_input, email)
        self.enter_data_in_field(
            create_account_page_locators.password_input, password)
