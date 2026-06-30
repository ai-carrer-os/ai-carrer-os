from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    original_filename: str
    stored_filename: str

    model_config = {
        "from_attributes": True
    }