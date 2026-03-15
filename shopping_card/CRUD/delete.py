from sqlalchemy import delete

async def remove_movie_from_cart(cart_id: int, movie_id: int, db: AsyncSession):

    await db.execute(
        delete(CartItem).where(
            CartItem.cart_id == cart_id,
            CartItem.movie_id == movie_id
        )
    )

    await db.commit()
