import stripe
from fastapi import Request

from app.config import STRIPE_WEBHOOK_SECRET


@router.post("/webhook/stripe")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except Exception:
        raise HTTPException(400, "Invalid webhook")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        order_id = session["metadata"]["order_id"]

        order = db.query(Order).filter_by(id=order_id).first()

        if order and order.status == OrderStatus.pending:
            order.status = OrderStatus.paid
            db.commit()

            send_email(order.user.email, "Payment successful")

    return {"status": "ok"}
