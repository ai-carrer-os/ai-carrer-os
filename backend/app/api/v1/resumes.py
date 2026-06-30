import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.resume import Resume
from app.services.resume_parser import extract_resume_text

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)

UPLOAD_DIR = Path("generated/resumes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    extension = Path(file.filename).suffix

    filename = f"{uuid4()}{extension}"

    filepath = UPLOAD_DIR / filename

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from resume
    text = extract_resume_text(str(filepath))

    # Save to database
    resume = Resume(
        user_id=1,  # Temporary (later we'll use JWT)
        original_filename=file.filename,
        stored_filename=filename,
        extracted_text=text,
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {
        "resume_id": resume.id,
        "message": "Resume uploaded successfully",
        "original_filename": file.filename,
        "stored_filename": filename,
        "characters": len(text),
        "preview": text[:1000]
    }