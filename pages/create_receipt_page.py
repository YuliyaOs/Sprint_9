from pages.base_page import BasePage
from locators import create_receipt_page_locators
import configuration
import os
import allure


class CreateReceiptPage(BasePage):

    @allure.step('Кликаем на кнопку "Создать рецепт" в хэдере сайта')
    def click_сreate_receipt_in_header(self):
        self.click_to_element(
            create_receipt_page_locators.create_receipt_in_header)
        self.wait_url_contains(configuration.CREATE_RECEIPT)

    @allure.step('Заполняем форму "Создать рецепт"')
    def input_create_receipt_form(self, name, ingredient, amount, time_c, description, file):
        self.enter_data_in_field(
            create_receipt_page_locators.name_receipt, name)
        self.enter_data_in_field(
            create_receipt_page_locators.ingredients, ingredient)
        self.click_to_element(create_receipt_page_locators.lemonade)
        self.enter_data_in_field(create_receipt_page_locators.amount, amount)
        self.click_to_element(create_receipt_page_locators.add_ingredient)
        self.enter_data_in_field(create_receipt_page_locators.time, time_c)
        self.enter_data_in_field(
            create_receipt_page_locators.description, description)
        file_path = os.path.abspath(file)
        self.wait_presence_of_element(
            create_receipt_page_locators.file_on_page).send_keys(file_path)
        self.click_to_element(
            create_receipt_page_locators.create_receipt_button)
        self.wait_url_not_contains('create')
        change_receipt_button = self.find_element(
            create_receipt_page_locators.change_receipt)
        self.wait_visibility_of_element(
            create_receipt_page_locators.title_receipt)
        title_receipt = self.find_element(
            create_receipt_page_locators.title_receipt)
        return change_receipt_button, title_receipt
