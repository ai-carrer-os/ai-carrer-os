from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.db.database import Base, engine

# Import models so SQLAlchemy knows about them
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerPilot AI",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to CareerPilot AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }