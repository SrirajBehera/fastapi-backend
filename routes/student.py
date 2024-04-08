from fastapi import APIRouter, HTTPException, status, Query, Path
from models.student import Student, StudentPatch
from config.db import student_collection
from typing import Optional
from bson.objectid import ObjectId
from schemas.student import student_entity

student_router = APIRouter()


@student_router.post("/students",
                     description="API to create a student in the system. All fields are mandatory and required while creating the student in the system.",
                     status_code=status.HTTP_201_CREATED,
                     responses={
                         status.HTTP_201_CREATED: {
                             "description": "A JSON response sending back the ID of the newly created student record.",
                             "content": {
                                 "application/json": {
                                     "schema": {
                                         "type": "object",
                                         "properties": {
                                             "id": {
                                                 "type": "string"
                                             }
                                         }
                                     }
                                 }
                             }
                         }
                     }
                     )
async def create_student(student: Student):
    try:
        student_id = await student_collection.insert_one(student.dict())
        return {"id": str(student_id.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@student_router.get("/students", status_code=status.HTTP_200_OK,
                    description="An API to find a list of students. You can apply filters on this API by passing the query parameters as listed below.",
                    responses={
                        status.HTTP_200_OK: {
                            "description": "sample response",
                            "content": {
                                 "application/json": {
                                     "schema": {
                                         "type": "object",
                                         "properties": {
                                             "data": {
                                                 "type": "array",
                                                 "items": {
                                                     "type": "object",
                                                     "properties": {
                                                         "name": {
                                                             "type": "string"
                                                         },
                                                         "age": {
                                                             "type": "integer"
                                                         }
                                                     }
                                                 }
                                             }
                                         }
                                     }
                                 }
                             }
                        }
                    })
async def list_students(
        country: Optional[str] = Query(None,
                                       description="To apply filter of country. If not given or empty, this filter should be applied."),
        age: Optional[int] = Query(None,
                                   description="Only records which have age greater than equal to the provided age should be present in the result. If not given or empty, this filter should be applied.")
):
    try:
        query = {}
        if country:
            query["address.country"] = country
        if age:
            query["age"] = {"$gte": age}
        students = await student_collection.find(query).to_list(length=None)
        return {"data": [{"name": student["name"], "age": student["age"]} for student in students]}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@student_router.get("/students/{id}", response_model=Student, status_code=status.HTTP_200_OK,
                    responses={
                        status.HTTP_200_OK: {
                            "description": "sample response"
                        }
                    })
async def get_student(id: str = Path(..., description="The ID of the student previously created.")):
    try:
        student = await student_collection.find_one({"_id": ObjectId(id)})
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return student_entity(student)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@student_router.patch("/students/{id}", status_code=status.HTTP_204_NO_CONTENT,
                      description="API to update the student's properties based on information provided. Not mandatory that all information would be sent in PATCH, only what fields are sent should be updated in the Database.",
                      responses={
                          status.HTTP_204_NO_CONTENT: {
                              "description": "No content",
                              "content": {
                                  "application/json": {
                                      "schema": {
                                          "type": "object"
                                      }
                                  }
                              }
                          }
                      })
async def update_student(
        student_update: StudentPatch,
        id: str = Path(..., description="The ID of the student previously created."),
):
    try:
        student = await student_collection.find_one({"_id": ObjectId(id)})
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

        if student_update.name is not None:
            student["name"] = student_update.name
        if student_update.age is not None:
            student["age"] = student_update.age
        if student_update.address:
            if student_update.address.city is not None:
                student["address"]["city"] = student_update.address.city
            if student_update.address.country is not None:
                student["address"]["country"] = student_update.address.country

        await student_collection.update_one({"_id": ObjectId(id)}, {"$set": student})

        return {}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@student_router.delete("/students/{id}", status_code=status.HTTP_200_OK,
                       responses={
                           status.HTTP_200_OK: {
                               "description": "sample response",
                               "content": {
                                   "application/json": {
                                       "schema": {
                                           "type": "object"
                                       }
                                   }
                               }
                           }
                       })
async def delete_student(id: str = Path(..., description="The ID of the student previously created.")):
    try:
        result = await student_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return {}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))