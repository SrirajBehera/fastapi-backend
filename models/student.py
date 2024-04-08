from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    """
    A model representing the address of a student.

    Attributes:
        city (str): The city name.
        country (str): The country name.
    """
    city: str = Field(..., description="city name")
    country: str = Field(..., description="country name")


class Student(BaseModel):
    """
    A model representing a student.

    Attributes:
        name (str): The student's name.
        age (int): The student's age.
        address (Address): The student's address.
    """
    name: str = Field(..., description="student's name")
    age: int = Field(..., description="student's age")
    address: Address


class AddressPatch(BaseModel):
    """
    A model representing a partial update to a student's address.

    Attributes:
        city (Optional[str]): The updated city name, or None if not updated.
        country (Optional[str]): The updated country name, or None if not updated.
    """
    city: Optional[str] = Field(None, description="city name")
    country: Optional[str] = Field(None, description="country name")


class StudentPatch(BaseModel):
    """
    A model representing a partial update to a student.

    Attributes:
        name (Optional[str]): The updated student name, or None if not updated.
        age (Optional[int]): The updated student age, or None if not updated.
        address (Optional[AddressPatch]): The updated student address, or None if not updated.
    """
    name: Optional[str] = Field(None, description="student's name")
    age: Optional[int] = Field(None, description="student's age")
    address: Optional[AddressPatch] = None
