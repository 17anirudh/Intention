from typing import Literal
from pydantic import BaseModel
from enum import Enum
from fastapi import UploadFile

class TypeEnum(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    IMAGE = Literal["png", "jpg", "jpeg", "gif", "bmp", "tiff", "webp"]
    
class DocumentRequest(BaseModel):
    file: UploadFile

class DocumentResponse(BaseModel):
    data: str