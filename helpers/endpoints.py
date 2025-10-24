class Endpoints:
    """Файл с всеми URL-адресами API для удобства использования"""

    # Базовый URL API Stellar Burgers
    BASE_URL = "https://stellarburgers.education-services.ru/api"

    # Эндпоинты для работы с пользователями
    REGISTER = f"{BASE_URL}/auth/register"  # Создание пользователя
    LOGIN = f"{BASE_URL}/auth/login"  # Логин пользователя
    USER = f"{BASE_URL}/auth/user"  # Получение/обновление данных пользователя

    # Эндпоинты для работы с заказами
    ORDERS = f"{BASE_URL}/orders"  # Создание заказа
    INGREDIENTS = f"{BASE_URL}/ingredients"  # Получение ингредиентов