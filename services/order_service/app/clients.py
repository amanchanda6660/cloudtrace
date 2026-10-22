import httpx

INVENTORY_SERVICE_URL = "http://127.0.0.1:8001/inventory/check"


def check_inventory(sku: str, quantity: int) -> dict:
    response = httpx.post(
        INVENTORY_SERVICE_URL,
        json={"sku": sku, "quantity": quantity},
        timeout=5.0,
    )
    response.raise_for_status()
    return response.json()
