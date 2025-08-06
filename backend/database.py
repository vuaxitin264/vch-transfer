"""
Database configuration for the VCH Transfer backend.

This module creates a SQLAlchemy engine, a session factory, and a declarative base
for defining models. The database URL can be configured via the `DATABASE_URL`
environment variable. By default it points to a local PostgreSQL instance.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Use an environment variable to configure the database connection. Fall back to a
# sensible default for local development.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/vch_transfer",
)

# Create the SQLAlchemy engine and session factory.
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models.
Base = declarative_base()
