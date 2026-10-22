from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_available_inventory():
    response = client.post(
        "/inventory/check",
        json={"sku": "laptop", "quantity": 2},
    )

    assert response.status_code == 200
    assert response.json()["available"] is True


def test_insufficient_inventory():
    response = client.post(
        "/inventory/check",
        json={"sku": "laptop", "quantity": 20},
    )

    assert response.status_code == 200
    assert response.json()["available"] is False


def test_unknown_sku():
    response = client.post(
        "/inventory/check",
        json={"sku": "phone", "quantity": 1},
    )

    assert response.status_code == 200
    assert response.json()["available"] is False


def test_invalid_quantity():
    response = client.post(
        "/inventory/check",
        json={"sku": "laptop", "quantity": 0},
    )

    assert response.status_code == 422
