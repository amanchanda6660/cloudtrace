from fastapi import FastAPI, HTTPException

from .clients import check_inventory
from .models import OrderRequest, OrderResponse

app = FastAPI(title="CloudTrace Order Service")


@app.post("/orders", response_model=OrderResponse)
def create_order(request: OrderRequest) -> OrderResponse:
    try:
        inventory = check_inventory(request.sku, request.quantity)
    except Exception as error:
        raise HTTPException(status_code=503, detail="Inventory Service unavailable") from error

    status = "accepted" if inventory["available"] else "rejected"

    return OrderResponse(
        status=status,
        sku=request.sku,
        quantity=request.quantity,
    )
