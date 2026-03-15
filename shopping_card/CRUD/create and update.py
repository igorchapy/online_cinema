from sqlalchemy import select
from models import Cart
from sqlalchemy.ext.asyncio import AsyncSession


async def get_or_create_cart(user_id: int, db: AsyncSession):

    result = await db.execute(
        select(Cart).where(Cart.user_id == user_id)
    )

    cart = result.scalar_one_or_none()

    if not cart:
        cart = Cart(user_id=user_id)
        db.add(cart)
        await db.commit()
        await db.refresh(cart)

    return cart
