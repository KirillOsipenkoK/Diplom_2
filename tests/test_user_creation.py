import pytest
import allure
from api_client.api_client import StellarBurgersAPI
from helpers.data import USER_TEST_DATA


class TestUserCreation:

    @allure.title("Успешное создание пользователя")
    def test_create_user_success(self, create_and_delete_user):
        api_client, email, password, name = create_and_delete_user

        with allure.step("Проверяем успешное создание"):
            response = api_client.register_user(email, password, name)
            assert response.status_code == 200, f"Код должен быть 200, получен {response.status_code}"

            response_data = response.json()
            assert response_data["success"] == True, "Должен быть success: true"
            assert "accessToken" in response_data, "Должен вернуться accessToken"
            assert "refreshToken" in response_data, "Должен вернуться refreshToken"
            assert response_data["user"]["email"] == email, "Email должен совпадать"
            assert response_data["user"]["name"] == name, "Name должен совпадать"

    @allure.title("Создание пользователя с существующим email")
    def test_create_duplicate_user(self, create_and_delete_user):
        api_client, email, password, name = create_and_delete_user
        response = api_client.register_user(email, password, name)

        with allure.step("Пытаемся создать дубликат пользователя"):
            response = api_client.register_user(email, "different_password", "different_name")

        with allure.step("Проверяем ошибку конфликта"):
            assert response.status_code == 403, f"Должна быть ошибка 403, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] == False, "Должен быть success: false"
            assert "already exists" in response_data["message"], "Должно быть сообщение о существующем пользователе"

    @pytest.mark.parametrize("field_name", ["missing_email", "missing_password", "missing_name"])
    @allure.title("Создание пользователя без обязательного поля: {field_name}")
    def test_create_user_missing_fields(self, field_name):
        api_client = StellarBurgersAPI()
        with allure.step(f"Отправляем запрос без поля {field_name}"):
            payload = USER_TEST_DATA[field_name]
            # Исправленная передача параметров
            email = payload.get("email", "")
            password = payload.get("password", "")
            name = payload.get("name", "")
            response = api_client.register_user(email, password, name)

        with allure.step("Проверяем ошибку клиента"):
            assert response.status_code == 403, f"Код должен быть 403, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] == False, "Должен быть success: false"
            assert "required" in response_data["message"].lower(), "Должно быть сообщение об обязательных полях"
