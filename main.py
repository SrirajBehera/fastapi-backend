from fastapi import FastAPI
from routes.student import student_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI on Render!"}


app.include_router(student_router, prefix="/api")
