from api_framework.base_api import BaseApi
import configuration
import allure


class UserApi(BaseApi):

    @allure.step('Создаем пользователя')
    def create_user(self, first_name, last_name, username, email, password):
        payload = {"email": email,
                   "password": password,
                   "username": username,
                   "first_name": first_name,
                   "last_name": last_name}
        response = self.post_request(
            configuration.URL_BACKEND, data=payload)
        return response

    @allure.step('Авторизуем пользователя')
    def login_user(self, username, password):
        payload = {"email": username,
                   "password": password}
        response = self.post_request(
            configuration.LOGIN_USER, data=payload)
        return response
