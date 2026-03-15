from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from schemas import CartItemCreate
from crud import add_movie_to_cart

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/items")
async def add_item(
    item: CartItemCreate,
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await add_movie_to_cart(user_id, item.movie_id, db)
