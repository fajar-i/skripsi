"""
LogiTrace: Main FastAPI Application Entrypoint.
Provides REST and WebSocket interfaces for adaptive evaluation in Station Rotation.
"""

from contextlib import asynccontextmanager
import logging
import os
from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI, Depends

load_dotenv()
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .db.database import init_db, get_db, AsyncSessionLocal
from .db.models import Interaction, Student
from .db.seeder import seed_database
from .routers import student_quiz, teacher_ambient, session_management

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("logitrace_app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure tables exist and initial curriculum seed is present
    logger.info("Initializing LogiTrace database...")
    await init_db()
    async with AsyncSessionLocal() as session:
        counts = await seed_database(session)
        logger.info(f"Database seed status: {counts}")
    yield
    # Shutdown
    logger.info("Shutting down LogiTrace application...")


app = FastAPI(
    title="LogiTrace API",
    description="Platform Web Evaluasi Formatif Adaptif Berbasis Knowledge Tracing & RAG dalam Station Rotation SMK TKJ",
    version="2.0.0",
    lifespan=lifespan
)

# Enable CORS for local laboratory smartphone access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(student_quiz.router)
app.include_router(teacher_ambient.router)
app.include_router(session_management.router)

# Mount Frontend & Documentation Static Directories
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend"))
DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs"))
STUDENT_DIR = os.path.join(FRONTEND_DIR, "student")
TEACHER_DIR = os.path.join(FRONTEND_DIR, "teacher")

if os.path.exists(STUDENT_DIR):
    app.mount("/student", StaticFiles(directory=STUDENT_DIR, html=True), name="student")

if os.path.exists(TEACHER_DIR):
    app.mount("/teacher", StaticFiles(directory=TEACHER_DIR, html=True), name="teacher")

if os.path.exists(DOCS_DIR):
    app.mount("/documentation", StaticFiles(directory=DOCS_DIR, html=True), name="documentation")


@app.get("/", response_class=HTMLResponse)
async def portal_root():
    """Hub portal & flagship landing page for LogiTrace Station Rotation System."""
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>LogiTrace API v2.0.0</h1><p><a href='/student/'>Portal Siswa</a> | <a href='/teacher/'>Dasbor Guru</a></p>"



@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "LogiTrace RAG-KT Backend",
        "version": "2.0.0",
        "engine": "Deterministic L3 Runtime (< 1 ms)"
    }


@app.get("/api/export/audit-logs")
async def export_audit_logs(db: AsyncSession = Depends(get_db)):
    """
    US-07: Integritas Audit Trail & Ekspor Data Analisis Dosis-Respons.
    Exports anonymous append-only interaction logs for scientific evaluation (E1 - E6).
    """
    stmt = (
        select(
            Interaction.id,
            Student.anonymous_code,
            Interaction.item_id,
            Interaction.session_number,
            Interaction.sequence_number,
            Interaction.response_result,
            Interaction.student_choice,
            Interaction.predicted_p,
            Interaction.mastery_before,
            Interaction.mastery_after,
            Interaction.response_time_ms,
            Interaction.hint_level_used,
            Interaction.is_calibration,
            Interaction.created_at
        )
        .join(Student, Interaction.student_id == Student.id)
        .order_by(Interaction.created_at)
    )
    res = await db.execute(stmt)
    rows = res.all()

    export_records = []
    for r in rows:
        export_records.append({
            "interaction_id": r[0],
            "anonymous_code": r[1],
            "item_id": r[2],
            "session_number": r[3],
            "sequence_number": r[4],
            "response_result": r[5],
            "student_choice": r[6],
            "predicted_p": r[7],
            "mastery_before": r[8],
            "mastery_after": r[9],
            "response_time_ms": r[10],
            "hint_level_used": r[11],
            "is_calibration": r[12],
            "created_at": r[13].isoformat()
        })

    return {
        "record_count": len(export_records),
        "audit_policy": "Strictly Append-Only (SQL UPDATE/DELETE Prohibited)",
        "records": export_records
    }
