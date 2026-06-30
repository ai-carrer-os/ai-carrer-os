from sqlalchemy import Column, ForeignKey, Integer, String, Text

from app.db.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    original_filename = Column(String(255))

    stored_filename = Column(String(255))

    extracted_text = Column(Text)