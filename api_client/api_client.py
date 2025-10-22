import requests
import allure
from helpers.endpoints import Endpoints


class StellarBurgersAPI:
    """API клиент для работы с Stellar Burgers"""

    def __init__(self):
        self.session = requests.Session()
        self.token = None

    @allure.step("Регистрация пользователя")
    def register_user(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = self.session.post(Endpoints.REGISTER, json=payload)
        if response.status_code == 200:
            data = response.json()
            self.token = data.get('accessToken')
        return response

    @allure.step("Авторизация пользователя")
    def login_user(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = self.session.post(Endpoints.LOGIN, json=payload)
        if response.status_code == 200:
            data = response.json()
            self.token = data.get('accessToken')
        return response

    @allure.step("Создание заказа")
    def create_order(self, ingredients, auth=False):
        payload = {
            "ingredients": ingredients
        }
        headers = {}
        if auth and self.token:
            headers['Authorization'] = self.token
        response = self.session.post(Endpoints.ORDERS, json=payload, headers=headers)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self):
        if not self.token:
            return None
        headers = {'Authorization': self.token}
        response = self.session.delete(Endpoints.USER, headers=headers)
        return response

    @allure.step("Получение данных пользователя")
    def get_user_data(self):
        if not self.token:
            return None
        headers = {'Authorization': self.token}
        response = self.session.get(Endpoints.USER, headers=headers)
        return response