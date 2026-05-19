from selenium.webdriver.common.by import By

create_receipt_in_header = [By.XPATH, ".//a[text()='Создать рецепт']"]
name_receipt = [
    By.XPATH, ".//div[text()='Название рецепта']/following-sibling::input"]
ingredients = [
    By.XPATH, ".//div[text()='Ингредиенты']/following-sibling::input"]
amount = [By.XPATH, ".//input[contains(@class,'Amount')]"]
lemonade = [By.XPATH, ".//div[text()='лимонад']"]
add_ingredient = [By.XPATH, ".//div[text()='Добавить ингредиент']"]
time = [
    By.XPATH, ".//div[text()='Время приготовления']/following-sibling::input"]
description = [
    By.XPATH, ".//div[text()='Описание рецепта']/following-sibling::textarea"]
file_on_page = [By.XPATH, "//input[@type='file']"]
create_receipt_button = [By.XPATH, ".//button[text()='Создать рецепт']"]
change_receipt = [By.XPATH, ".//a[text()='Редактировать рецепт']"]
title_receipt = [By.XPATH, ".//h1"]
