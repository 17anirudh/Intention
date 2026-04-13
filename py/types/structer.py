from enum import Enum
from pydantic import BaseModel, Field
from datetime import date
from document import TypeEnum
from typing import Optional, Tuple

class SeverityLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class HighPriorityIssue(str, Enum):
    ABUSE = "abuse"
    PHYSICAL_ABUSE = "physical abuse"
    DOMESTIC_VIOLENCE = "domestic violence"
    MEDICAL_EMERGENCY = "medical emergency"
    SUICIDAL_THOUGHTS = "suicidal thoughts"
    BASIC_AMENITIES = "basic amenities"

class MediumPriorityIssue(str, Enum):
    CULTURAL_DISPUTES = "cultural disputes"
    LOCAL_CULTURE_PRESERVATION = "local culture preservation"
    EDUCATION = "education"
    LOW_RISK_DISEASES = "low risk diseases"
    POWER_INTERNET_DISRUPTIONS = "power/internet disruptions"
    DEFORESTATION = "deforestation"
    ANIMAL_ABUSE = "animal abuse"
    CORRUPTION = "corruption"
    SCHOLARSHIPS = "scholarships"
    SANITIZATION = "sanitization"

class LowPriorityIssue(str, Enum):
    LAND_DISPUTES = "land disputes"
    ADULT_EDUCATION = "adult education"
    COMMUNITY_EVENTS = "community events"
    OTHERS = "others"

Classification = HighPriorityIssue | MediumPriorityIssue | LowPriorityIssue

class Points(BaseModel):
    title: str = Field(..., description="Title of a single observation")
    content: str = Field(..., description="Content of the observation")
    seriousness: float = Field(..., ge=0.0, le=1.0, description="Seriousness score between 0 and 1")
    classification: Classification = Field(..., description="Classification of the observation")

class DocumentStructure(BaseModel):
    title: str = Field(..., description="Title of the document")
    sections: list[str] = Field(..., description="List of sections in document")
    language: str = Field(..., max_length=80, description="Language of the document")
    date_conducted: date = Field(..., description="Date when the document was conducted")
    doc_types: list[TypeEnum] = Field(..., description="List of document types")
    items: list[Points] = Field(..., description="All the points in the document")
    summary: str = Field(..., min_length=10, max_length=1000, description="Summary of the document")
    location: Tuple[str, str, str] = Field(..., description="Location tuple: (city, district/county, country)")

class DocumentMetaData(BaseModel):
    name: str = Field(..., description="Name of the document")
    title: Optional[str] = Field(None, description="Title of the document")
    date_conducted: Optional[date] = Field(None, description="Date when the document was conducted")
    page_nums: Optional[int] = Field(None, description="Number of pages in the document")
    text: str = Field(..., description="Text of the document")