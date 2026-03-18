from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


class OrderItemResponse(BaseModel):
    movie_id: int
    price_at_order: Decimal

    class Config:
        orm_mode = True


class OrderResponse(BaseModel):
    id: int
    created_at: datetime
    status: str
    total_amount: Decimal
    items: list[OrderItemResponse]

    class Config:
        orm_mode = True
