import pytest
import requests



class TestCreateUser:
    def test_create_user_successfully(self):
        url = "https://playground.learnqa.ru/api/user/"
        data = {
            "username": "JohnDoe",
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "secure_123_passw"
        }
        
        response = requests.post(url, data=data)
        
        assert response.status_code == 200, "Failed to create user"
        
        response_data = response.json()
        
        assert "id" in response_data, "User ID not found in response"
        
        user_id = response_data["id"]
        
        print(f"User created successfully with ID: {user_id}")
        
        















