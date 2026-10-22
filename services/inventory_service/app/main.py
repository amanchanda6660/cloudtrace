from fastapi import FastAPI

from .models import InventoryCheckRequest, InventoryCheckResponse

app = FastAPI(title="CloudTrace Inventory Service")

INVENTORY = {
    "laptop": 10,
    "keyboard": 25,
}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/inventory/check", response_model=InventoryCheckResponse)
def check_inventory(request: InventoryCheckRequest) -> InventoryCheckResponse:
    available_quantity = INVENTORY.get(request.sku, 0)

    return InventoryCheckResponse(
        sku=request.sku,
        requested_quantity=request.quantity,
        available_quantity=available_quantity,
        available=available_quantity >= request.quantity,
    )
