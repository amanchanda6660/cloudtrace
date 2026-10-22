from pydantic import BaseModel, Field


class InventoryCheckRequest(BaseModel):
    sku: str = Field(min_length=1)
    quantity: int = Field(gt=0)


class InventoryCheckResponse(BaseModel):
    sku: str
    requested_quantity: int
    available_quantity: int
    available: bool

