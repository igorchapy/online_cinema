from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from db import get_db
from services.payment_service import PaymentService
from schemas.payment import PaymentCreate
from core.config import settings

import stripe

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/")
def create_payment(
    data: PaymentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    try:
        payment, client_secret = PaymentService.create_payment(
            db, user, data.order_id
        )

        return {
            "payment_id": payment.id,
            "client_secret": client_secret
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):

    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid webhook")

    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        PaymentService.handle_success(db, intent["id"])

    elif event["type"] == "payment_intent.payment_failed":
        intent = event["data"]["object"]
        PaymentService.handle_failed(db, intent["id"])

    return {"ok": True}


@router.get("/")
def get_my_payments(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return db.query(Payment).filter(
        Payment.user_id == user.id
    ).all()
