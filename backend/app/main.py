from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes.students import router as student_router


# Import models so SQLAlchemy knows about them
from app.models.student import Student


# Create database tables
Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Mastermind Academy API",
    description="Academy Management System",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(
    student_router
)


@app.get("/")
def root():

    return {
        "application": "Mastermind Academy",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():

    return {
        "status": "UP",
        "application": "Mastermind Academy"
    }