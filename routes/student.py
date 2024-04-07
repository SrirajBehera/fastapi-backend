from fastapi import APIRouter, HTTPException, status, Query, Path
from models.student import Student
from config.db import student_collection
from typing import Optional
from bson.objectid import ObjectId
from schemas.student import student_entity, students_entity

student_router = APIRouter()


@student_router.post("/students", status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    student_id = await student_collection.insert_one(student.dict())
    return {"id": str(student_id.inserted_id)}


@student_router.get("/students", status_code=status.HTTP_200_OK)
async def list_students(
        country: Optional[str] = Query(None, description="To apply filter of country. If not given or empty, this filter should be applied."),
        age: Optional[int] = Query(None, description="Only records which have age greater than equal to the provided age should be present in the result. If not given or empty, this filter should be applied.")
):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = await student_collection.find(query).to_list(length=None)
    # return students_entity(students)
    return {"data": [{"name": student["name"], "age": student["age"]} for student in students]}


@student_router.get("/students/{id}", response_model=Student, status_code=status.HTTP_200_OK)
async def get_student(id: str = Path(..., description="The ID of the student previously created.")):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student_entity(student)


@student_router.patch("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_student(
        id: str = Path(..., description="The ID of the student previously created."),
        student_update: Student = {}
):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    update_data = student_update.dict(exclude_unset=True)
    if update_data:
        await student_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})

    return {}


@student_router.delete("/students/{id}", status_code=status.HTTP_200_OK)
async def delete_student(id: str = Path(..., description="The ID of the student previously created.")):
    result = await student_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return {}
