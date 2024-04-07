from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str = Field(..., description="city name")
    country: str = Field(..., description="country name")


class Student(BaseModel):
    name: str = Field(..., description="student's name")
    age: int = Field(..., description="student's age")
    address: Address
