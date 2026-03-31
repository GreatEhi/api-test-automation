import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    response = requests.get(f"{BASE_URL}/users")
    return response

def create_user(data):
    response = requests.post(f"{BASE_URL}/users", json=data)
    return response

def update_user(user_id, data):
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=data)
    return response

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    return response