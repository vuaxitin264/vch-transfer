"""
Reusable CRUD utility functions for interacting with the database.

These functions separate the database logic from the API layer and can be
imported wherever needed. They are deliberately simple for the purposes of
demonstration and do not include advanced error handling or validation.
"""

from sqlalchemy.orm import Session

from . import models, schemas


def get_invoices(db: Session, skip: int = 0, limit: int = 100) -> list[models.Invoice]:
    """Retrieve a list of invoices from the database with pagination."""
    return db.query(models.Invoice).offset(skip).limit(limit).all()


def get_invoice(db: Session, invoice_id: int) -> models.Invoice | None:
    """Retrieve a single invoice by its ID."""
    return db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()


def create_invoice(db: Session, invoice: schemas.InvoiceCreate) -> models.Invoice:
    """Create a new invoice in the database.

    The VND amount is calculated with a fixed exchange rate of 1 USD to 24,000 VND.
    """
    vnd_amount = invoice.amount_usd * 24000
    db_invoice = models.Invoice(
        sender_name=invoice.sender_name,
        recipient_name=invoice.recipient_name,
        amount_usd=invoice.amount_usd,
        amount_vnd=vnd_amount,
        status="pending",
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def update_invoice(db: Session, invoice_id: int, updated: schemas.InvoiceCreate) -> models.Invoice | None:
    """Update an existing invoice. Returns the updated invoice or `None` if not found."""
    invoice = get_invoice(db, invoice_id)
    if invoice is None:
        return None
    invoice.sender_name = updated.sender_name
    invoice.recipient_name = updated.recipient_name
    invoice.amount_usd = updated.amount_usd
    invoice.amount_vnd = updated.amount_usd * 24000
    db.commit()
    db.refresh(invoice)
    return invoice


def delete_invoice(db: Session, invoice_id: int) -> bool:
    """Delete an invoice by its ID. Returns `True` if deleted, `False` if not found."""
    invoice = get_invoice(db, invoice_id)
    if invoice is None:
        return False
    db.delete(invoice)
    db.commit()
    return True
