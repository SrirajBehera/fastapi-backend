"""
This script defines the main FastAPI application and includes the student API routes.

The script sets up the FastAPI application, configures the CORS middleware, and includes the student API router.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.student import student_router

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Root endpoint that returns a simple message.

    Returns:
        dict: A dictionary containing a "message" key with the value "Hello, FastAPI on Render!".
    """
    return {"message": "Hello, FastAPI on Render!"}


app.include_router(student_router, prefix="/api")
