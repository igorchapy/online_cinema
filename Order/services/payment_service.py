import stripe
from app.config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def create_checkout_session(order):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": f"Order #{order.id}",
                    },
                    "unit_amount": int(order.total_amount * 100),
                },
                "quantity": 1,
            }
        ],
        success_url=f"http://localhost:8000/success?order_id={order.id}",
        cancel_url=f"http://localhost:8000/cancel?order_id={order.id}",
        metadata={
            "order_id": order.id
        }
    )

    return session.url
