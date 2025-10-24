import pytest
import allure
from api_client.api_client import StellarBurgersAPI
from helpers.generator import generate_unique_email


@pytest.fixture
def user_data():
    """Фикстура с тестовыми данными пользователя"""
    return {
        "email": generate_unique_email(),
        "password": "password123",
        "name": "Test User"
    }


@pytest.fixture
def create_and_delete_user():
    """Фикстура для создания и удаления пользователя"""
    api_client = StellarBurgersAPI()

    with allure.step("Создаем пользователя"):
        email = generate_unique_email()
        password = "password123"
        name = "Test User"

    yield api_client, email, password, name

    with allure.step("Удаляем пользователя"):
        if api_client.token:
            api_client.delete_user()


@pytest.fixture
def authenticated_user():
    """Фикстура для аутентифицированного пользователя"""
    api_client = StellarBurgersAPI()

    with allure.step("Регистрируем и логиним пользователя"):
        email = generate_unique_email()
        password = "password123"
        name = "Test User"

        api_client.register_user(email, password, name)
        api_client.login_user(email, password)

    yield api_client

    with allure.step("Удаляем пользователя"):
        if api_client.token:
            api_client.delete_user()
