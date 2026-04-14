from pydantic import BaseModel, constr, Field, EmailStr, PositiveInt
from enum import Enum
from typing import BinaryIO, Optional, Union

class DaysofWeek(str, Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

class Volunteer(BaseModel):
    name: constr(min_length=3, max_length=108) = Field(..., description="Volunteer name")
    phone: constr(min_length=10, max_length=15) = Field(..., description="Volunteer phone number")
    email: EmailStr = Field(..., description="Volunteer email")
    location: tuple(constr(max_length=50), constr(max_length=50), constr(max_length=50)) = Field(..., description="Location of the volunteer (city, district/county, country)")

    skills: list[str] = Field(..., description="List of skills of the volunteer")
    availability: list[DaysofWeek] = Field(..., description="List of days when the volunteer is available")
    experience: PositiveInt = Field(..., description="Years of experience")
    languages: list[constr(max_length=80)] = Field(..., description="Known languages")
    
    resume: Optional[Union[str, BinaryIO]] = Field(default=None, description="Resume file path or binary data") 
    notes: Optional[str] = Field(default=None, description="Additional notes about the volunteer")