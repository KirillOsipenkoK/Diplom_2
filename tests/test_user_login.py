import allure
from api_client.api_client import StellarBurgersAPI
from helpers.data import USER_TEST_DATA


class TestUserLogin:

    @allure.title("Успешный логин пользователя")
    def test_login_user_success(self, create_and_delete_user):
        api_client, email, password, name = create_and_delete_user
        response = api_client.register_user(email, password, name)

        with allure.step("Выполняем логин"):
            response = api_client.login_user(email, password)

        with allure.step("Проверяем успешный логин"):
            assert response.status_code == 200, f"Код должен быть 200, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] == True, "Должен быть success: true"
            assert "accessToken" in response_data, "Должен вернуться accessToken"
            assert "refreshToken" in response_data, "Должен вернуться refreshToken"
            assert response_data["user"]["email"] == email, "Email должен совпадать"
            assert response_data["user"]["name"] == name, "Name должен совпадать"

    @allure.title("Логин с неправильным паролем")
    def test_login_wrong_password(self, create_and_delete_user):
        api_client, email, password, name = create_and_delete_user
        response = api_client.register_user(email, password, name)

        with allure.step("Пытаемся логиниться с неправильным паролем"):
            response = api_client.login_user(email, "wrong_password")

        with allure.step("Проверяем ошибку"):
            assert response.status_code == 401, f"Должна быть ошибка 401, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] == False, "Должен быть success: false"
            assert "incorrect" in response_data["message"], "Должно быть сообщение о неверных данных"

    @allure.title("Логин несуществующего пользователя")
    def test_login_nonexistent_user(self):
        api_client = StellarBurgersAPI()
        with allure.step("Пытаемся логиниться несуществующим пользователем"):
            test_data = USER_TEST_DATA["invalid_login"]
            response = api_client.login_user(test_data["email"], test_data["password"])

        with allure.step("Проверяем ошибку"):
            assert response.status_code == 401, f"Должна быть ошибка 401, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] == False, "Должен быть success: false"
            assert "incorrect" in response_data["message"], "Должно быть сообщение о неверных данных"