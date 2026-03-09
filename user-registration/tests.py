import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db, Base, engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

def test_register_user_success(client):
    response = client.post("/register", json={
        "email": "user@example.com",
        "username": "user123",
        "password": "StrongPass123"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "User registered successfully"

def test_register_existing_email(client):
    client.post("/register", json={
        "email": "existing@example.com",
        "username": "existing_user",
        "password": "Password123"
    })
    response = client.post("/register", json={
        "email": "existing@example.com",
        "username": "another_user",
        "password": "Password123"
    })
    assert response.status_code == 400
    assert response.json()["error"] == "Email already exists"

def test_register_invalid_email(client):
    response = client.post("/register", json={
        "email": "invalid-email",
        "username": "user_invalid",
        "password": "Password123"
    })
    assert response.status_code == 422


def test_register_short_password(client):
    response = client.post("/register", json={
        "email": "shortpass@example.com",
        "username": "user_shortpass",
        "password": "123"
    })
    assert response.status_code == 422
