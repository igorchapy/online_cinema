from sqlalchemy import select
from models import Cart
from fastapi import HTTPException


@router.get("/")
async def get_cart(user_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Cart).where(Cart.user_id == user_id)
    )

    cart = result.scalar_one_or_none()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    return cart
