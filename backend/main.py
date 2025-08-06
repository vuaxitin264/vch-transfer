"""
FastAPI application entry point for the VCH Transfer backend.

This module defines a minimal set of endpoints for managing invoices. It uses
SQLAlchemy for persistence and Pydantic schemas for request/response models.
"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


# Create the database tables if they do not exist. In a production deployment you
# would run migrations instead of automatic creation.
models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="VCH Transfer API", version="0.1.0")


def get_db():
    """Provide a SQLAlchemy session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/invoices", response_model=schemas.InvoiceList)
def list_invoices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Return a paginated list of invoices."""
    items = crud.get_invoices(db, skip=skip, limit=limit)
    total = len(items)
    return schemas.InvoiceList(items=items, total=total)


@app.get("/invoices/{invoice_id}", response_model=schemas.Invoice)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    """Return a single invoice by ID or raise 404 if not found."""
    invoice = crud.get_invoice(db, invoice_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice


@app.post("/invoices", response_model=schemas.Invoice, status_code=201)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    """Create a new invoice."""
    created = crud.create_invoice(db, invoice)
    return created


@app.put("/invoices/{invoice_id}", response_model=schemas.Invoice)
def update_invoice(invoice_id: int, invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    """Update an existing invoice."""
    updated = crud.update_invoice(db, invoice_id, invoice)
    if updated is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return updated


@app.delete("/invoices/{invoice_id}", status_code=204)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    """Delete an invoice. Returns 204 on success or 404 if not found."""
    deleted = crud.delete_invoice(db, invoice_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return None
