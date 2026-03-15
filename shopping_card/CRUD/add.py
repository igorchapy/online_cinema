from models import CartItem

async def add_movie_to_cart(user_id: int, movie_id: int, db: AsyncSession):

    cart = await get_or_create_cart(user_id, db)

    item = CartItem(
        cart_id=cart.id,
        movie_id=movie_id
    )

    db.add(item)

    try:
        await db.commit()
    except:
        await db.rollback()
        raise Exception("Movie already in cart")

    await db.refresh(item)

    return item
