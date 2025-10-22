import random
import string
from datetime import datetime

# Функция для генерации случайных строк (вынесено из api_client.py)
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_unique_email():
    """Генерация уникального email для тестов"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_str = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"test_{timestamp}_{random_str}@test.com"