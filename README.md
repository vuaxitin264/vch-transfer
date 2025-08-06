# VCH Transfer Web App

This repository contains the source code for a simple money‑transfer management application. The goal of this project is to provide a starting point for a VN–US money transfer service with invoice management and printing capabilities.

## Structure

- **backend/** – A FastAPI server configured with SQLAlchemy to persist invoices to a PostgreSQL database.
- **frontend/** – A minimal React application bootstrapped with Vite and TailwindCSS. It contains a placeholder dashboard ready for further development.

## Getting Started

### Backend

1. Install dependencies:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Configure your PostgreSQL connection string in a `.env` file or set the `DATABASE_URL` environment variable. The default in `database.py` points to:

   ```
   postgresql://user:password@localhost:5432/vch_transfer
   ```

3. Run the server:

   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Install dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:

   ```bash
   npm run dev
   ```

This will launch the React application on port 5173. Open your browser and navigate to `http://localhost:5173` to view the dashboard placeholder.

## Notes

This project is a starting point and **does not implement** the full set of features described in the original design (e.g., invoice CRUD operations in the UI, authentication, PDF printing, etc.). Those features can be built on top of the existing structure. Contributions are welcome!
