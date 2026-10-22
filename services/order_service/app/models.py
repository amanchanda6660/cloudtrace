from pydantic import BaseModel, Field


class OrderRequest(BaseModel):
    sku: str = Field(min_length=1)
    quantity: int = Field(gt=0)


class OrderResponse(BaseModel):
    status: str
    sku: str
    quantity: int
