from utils.api_client import get_users, create_user, update_user, delete_user

def test_get_users():
    response = get_users()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    new_user = {
        "name": "John Doe",
        "email": "john@example.com"
    }

    response = create_user(new_user)

    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_update_user():
    updated_data = {
        "name": "Jane Doe"
    }

    response = update_user(1, updated_data)

    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_delete_user():
    response = delete_user(1)
    assert response.status_code == 200