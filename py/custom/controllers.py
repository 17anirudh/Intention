from typing import Literal, Optional
from pydantic import BaseModel
from enum import Enum
from fastapi import UploadFile

class TypeEnum(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    IMAGE = Literal["png", "jpg", "jpeg", "gif", "bmp", "tiff", "webp"]
    
class IngestionRequest(BaseModel):
    file: list[UploadFile]

class IngestionResponse(BaseModel):
    status: Literal["success", "failure"]
    failed_files: Optional[list[str]]
    time_taken: str