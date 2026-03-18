from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from db import Base


class PaymentStatus(str, enum.Enum):
    pending = "pending"
    successful = "successful"
    failed = "failed"
    canceled = "canceled"
    refunded = "refunded"


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    status = Column(Enum(PaymentStatus), default=PaymentStatus.pending, nullable=False)

    amount = Column(Numeric(10, 2), nullable=False)

    external_payment_id = Column(String, unique=True)

    items = relationship("PaymentItem", back_populates="payment")


class PaymentItem(Base):
    __tablename__ = "payment_items"

    id = Column(Integer, primary_key=True)

    payment_id = Column(Integer, ForeignKey("payments.id", ondelete="CASCADE"), nullable=False)
    order_item_id = Column(Integer, ForeignKey("order_items.id", ondelete="CASCADE"), nullable=False)

    price_at_payment = Column(Numeric(10, 2), nullable=False)

    payment = relationship("Payment", back_populates="items")
    