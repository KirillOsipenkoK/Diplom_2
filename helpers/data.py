USER_TEST_DATA = {
    "missing_email": {"email": "", "password": "password123", "name": "Test User"},
    "missing_password": {"email": "test@test.com", "password": "", "name": "Test User"},
    "missing_name": {"email": "test@test.com", "password": "password123", "name": ""},
    "existing_user": {
        "email": "existing_user@test.com",
        "password": "password123",
        "name": "Existing User"
    },
    "invalid_login": {
        "email": "nonexistent@test.com",
        "password": "wrongpassword"
    }
}

ORDER_TEST_DATA = {
    "valid_ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"],
    "invalid_ingredients": ["invalid_hash_123", "another_invalid_hash"],
    "empty_ingredients": []
}