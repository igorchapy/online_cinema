from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


class PaymentCreate(BaseModel):
    order_id: int


class PaymentResponse(BaseModel):
    id: int
    order_id: int
    amount: Decimal
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
        