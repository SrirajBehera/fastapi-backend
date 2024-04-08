from pydantic import BaseModel, Field
from typing import Optional


class Address(BaseModel):
    city: str = Field(..., description="city name")
    country: str = Field(..., description="country name")


class Student(BaseModel):
    name: str = Field(..., description="student's name")
    age: int = Field(..., description="student's age")
    address: Address


class AddressPatch(BaseModel):
    city: Optional[str] = Field(None, description="city name")
    country: Optional[str] = Field(None, description="country name")


class StudentPatch(BaseModel):
    name: Optional[str] = Field(None, description="student's name")
    age: Optional[int] = Field(None, description="student's age")
    address: Optional[AddressPatch] = None
