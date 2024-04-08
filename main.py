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
    return {"message": "Hello, FastAPI on Render!"}


app.include_router(student_router, prefix="/api")
