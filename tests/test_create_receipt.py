import allure
from pages.create_receipt_page import CreateReceiptPage


class TestCreateReceipt:

    @allure.title('Создание рецепта')
    def test_create_receipt(self, driver_with_auth, data_for_create_receipt):
        create_receipt_page = CreateReceiptPage(driver_with_auth)
        create_receipt_page.click_сreate_receipt_in_header()
        change_receipt_button, title_receipt = create_receipt_page.input_create_receipt_form(
            *data_for_create_receipt)

        assert change_receipt_button.is_displayed(
        ) and title_receipt.text == data_for_create_receipt[0]
