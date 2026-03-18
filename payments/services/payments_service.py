import stripe
from sqlalchemy.orm import Session

from models.payment import Payment, PaymentStatus, PaymentItem
from models.order import Order


class PaymentService:

    @staticmethod
    def create_payment(db: Session, user, order_id: int):

        order = db.query(Order).filter(Order.id == order_id).first()

        if not order:
            raise Exception("Order not found")

        if order.user_id != user.id:
            raise Exception("Forbidden")

        if order.total_price <= 0:
            raise Exception("Invalid amount")

        intent = stripe.PaymentIntent.create(
            amount=int(order.total_price * 100),
            currency="usd",
            metadata={"order_id": order.id, "user_id": user.id},
        )

        payment = Payment(
            user_id=user.id,
            order_id=order.id,
            amount=order.total_price,
            status=PaymentStatus.pending,
            external_payment_id=intent.id,
        )

        db.add(payment)
        db.flush()


        for item in order.items:
            db.add(PaymentItem(
                payment_id=payment.id,
                order_item_id=item.id,
                price_at_payment=item.price
            ))

        db.commit()
        db.refresh(payment)

        return payment, intent.client_secret

    @staticmethod
    def handle_success(db: Session, intent_id: str):

        payment = db.query(Payment).filter(
            Payment.external_payment_id == intent_id
        ).first()

        if not payment:
            return

        if payment.status == PaymentStatus.successful:
            return  # idempotency

        payment.status = PaymentStatus.successful

        order = payment.order
        order.status = "paid"

        db.commit()

    @staticmethod
    def handle_failed(db: Session, intent_id: str):

        payment = db.query(Payment).filter(
            Payment.external_payment_id == intent_id
        ).first()

        if not payment:
            return

        payment.status = PaymentStatus.failed
        db.commit()
