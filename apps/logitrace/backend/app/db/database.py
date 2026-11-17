"""
LogiTrace: Database Connection & Async Session Manager.
SQLite by default; any SQLAlchemy async URL via LOGITRACE_DB_URL / DATABASE_URL.
"""

import os
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import declarative_base

# Default to local SQLite dev database if LOGITRACE_DB_URL / DATABASE_URL is not set
DATABASE_URL = (
    os.getenv("LOGITRACE_DB_URL")
    or os.getenv("DATABASE_URL")
    or f"sqlite+aiosqlite:///{os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'logitrace.db'))}"
)

# SQLite foreign key enforcement
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    connect_args=connect_args
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for providing database session to FastAPI routers."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


# Columns added after the first schema version: (table, column, SQL type).
_ADDED_COLUMNS = [
    ("items", "indikator_id", "VARCHAR(16)"),
    ("items", "bloom_level", "VARCHAR(4)"),
    ("items", "jonassen_phase", "VARCHAR(48)"),
    ("items", "label_status", "VARCHAR(32)"),
    ("students", "pin_hash", "VARCHAR(160)"),
    ("students", "pin_set_at", "DATETIME"),
    ("students", "device_token_hash", "VARCHAR(64)"),
    ("students", "device_login_at", "DATETIME"),
    ("quiz_sessions", "join_code", "VARCHAR(8)"),
]


def _migrate_sqlite(sync_conn) -> None:
    """Lightweight additive migration for existing SQLite dev databases."""
    from sqlalchemy import inspect, text

    insp = inspect(sync_conn)
    tables = set(insp.get_table_names())
    for table, column, sql_type in _ADDED_COLUMNS:
        if table in tables and column not in {c["name"] for c in insp.get_columns(table)}:
            sync_conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {sql_type}"))


async def init_db() -> None:
    """Initializes tables in database and applies additive column migrations."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        if "sqlite" in DATABASE_URL:
            await conn.run_sync(_migrate_sqlite)
