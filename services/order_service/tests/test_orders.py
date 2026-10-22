from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_order_is_accepted_when_inventory_available():
    response = client.post(
        "/orders", 
        json={"sku": "laptop", "quantity": 2},
    )

    assert response.status_code == 200
    assert response.json() == {
        "status":"accepted",
        "sku":"laptop",
        "quantity": 2,
    }

def test_order_is_rejected_when_inventory_insufficient():
    response = client.post(
        "/orders", 
        json={"sku":"laptop", "quantity": 20}
    )

    assert response.status_code == 200
    assert response.json() == {
        "status":"rejected", 
        "sku":"laptop", 
        "quantity": 20
    }

def test_order_rejects_invalid_quantity():
    response = client.post(
        "/orders",
        json={"sku":"laptop", "quantity": 0}
    )

    assert response.status_code == 422