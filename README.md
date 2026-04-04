# API Test Automation Framework

A Python-based API test automation framework built using `pytest` and `requests`, covering basic CRUD operations.

## 📌 Features
- Automated API testing (GET, POST, PUT, DELETE)
- Status code validation
- Response body validation
- Clean and simple project structure

## 🛠️ Tech Stack
- Python
- Pytest
- Requests

## 📂 Project Structure

api-test-automation/
│
├── tests/
│ └── test_users.py
│
├── utils/
│ └── api_client.py
│
├── requirements.txt
└── README.md


## ▶️ How to Run Tests

1. Clone the repository:

git clone <your-repo-link>
cd api-test-automation

2. Create virtual environment:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Run tests:

pytest -v

## ✅ Test Coverage
- Get Users
- Create User
- Update User
- Delete User
