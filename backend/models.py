"""
SQLAlchemy ORM models for the VCH Transfer backend.

Currently only the `Invoice` model is defined. You can extend this file with
additional models for users, senders, recipients, etc. as your application grows.
"""

import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from .database import Base


class Invoice(Base):
    """Represents a money transfer invoice between a sender and a recipient."""

    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String, index=True)
    recipient_name = Column(String, index=True)
    amount_usd = Column(Float)
    amount_vnd = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self) -> str:
        return (
            f"Invoice(id={self.id!r}, sender_name={self.sender_name!r}, "
           f"recipient_name={self.recipient_name!r}, amount_usd={self.amount_usd!r}, "
            f"amount_vnd={self.amount_vnd!r}, status={self.status!r})"
        )
