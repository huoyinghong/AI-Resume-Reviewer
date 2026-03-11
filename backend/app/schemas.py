from pydantic import BaseModel


class ResumeParseResponse(BaseModel):
    filename: str
    text_preview: str
    text_length: int