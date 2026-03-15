from pydantic import BaseModel
from datetime import datetime


class CartItemCreate(BaseModel):
    movie_id: int


class CartItemResponse(BaseModel):
    id: int
    movie_id: int
    added_at: datetime

    class Config:
        from_attributes = True


class CartResponse(BaseModel):
    id: int
    user_id: int
    items: list[CartItemResponse]

    class Config:
        from_attributes = True
