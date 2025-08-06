# VCH Transfer Backend

This folder contains a minimal FastAPI backend for managing money transfer invoices. It uses SQLAlchemy to persist data to a PostgreSQL database.

## Features

- Define an `Invoice` model with fields for sender and recipient names, amounts in USD and VND, status, and creation time.
- Provide CRUD endpoints to create, read, update, delete, and list invoices.
- Convert USD amounts to VND using a fixed exchange rate (24,000 VND per 1 USD).

## Running

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure your database by setting the `DATABASE_URL` environment variable. Example:

   ```bash
   export DATABASE_URL=postgresql://user:password@localhost:5432/vch_transfer
   ```

3. Start the server using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`. Visit `/docs` for interactive Swagger UI.
