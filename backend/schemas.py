"""
Pydantic schemas for serializing and validating request and response data.

These schemas help FastAPI generate OpenAPI documentation and enforce type
checks when your API is called. Modify or extend them as needed.
"""

import datetime
from typing import Optional

from pydantic import BaseModel, Field


class InvoiceBase(BaseModel):
    sender_name: str = Field(..., example="John Smith")
    recipient_name: str = Field(..., example="Nguyen Van A")
    amount_usd: float = Field(..., gt=0, example=100.0)


class InvoiceCreate(InvoiceBase):
    """Data required to create a new invoice."""
    pass


class Invoice(InvoiceBase):
    """Represents an invoice stored in the database."""

    id: int
    amount_vnd: float
    status: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class InvoiceList(BaseModel):
    """A wrapper for returning multiple invoices in a single response."""

    items: list[Invoice]
    total: int
