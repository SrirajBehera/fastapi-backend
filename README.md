# FastAPI Backend

## Demo
Server hosted on Render: https://fastapi-backend-1-kvib.onrender.com
## Overview

This project is a FastAPI backend application that provides a RESTful API for managing student records. The application includes the following key features:

**Student Management**:
   - Create a new student record
   - List student records with optional filtering by country and age
   - Retrieve a specific student record
   - Update a specific student record
   - Delete a specific student record

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python.
- **MongoDB**: A NoSQL database used for storing student records.
- **Motor** (AsyncIOMotorClient): An asynchronous Python driver for MongoDB.
- **Pydantic**: A data validation and settings management library used for defining the data models.

## File Structure

The project has the following file structure:

```
.
├── main.py
├── .gitignore
├── .env
├── routes
│   └── student.py
├── models
│   └── student.py
├── config
│   └── db.py
└── schemas
    └── student.py
```

- `main.py`: This is the main script that sets up the FastAPI application, configures the CORS middleware, and includes the student API router.
- `.gitignore`: This is the .gitignore file.
- `.env`: This is the .env file.
- `routes/student.py`: This script defines the API endpoints for managing student records, including the following:
  - `POST /students`: Create a new student record
  - `GET /students`: List student records with optional filtering
  - `GET /students/{id}`: Retrieve a specific student record
  - `PATCH /students/{id}`: Update a specific student record
  - `DELETE /students/{id}`: Delete a specific student record
- `models/student.py`: This script defines the Pydantic models for the student data, including the `Student` and `StudentPatch` models.
- `config/db.py`: This script sets up the connection to the MongoDB database using the AsyncIOMotorClient.
- `schemas/student.py`: This script defines the schema for converting a MongoDB document to a Python dictionary for the student entity.

## Setup and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/SrirajBehera/fastapi-backend.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   - Create a `.env` file in the project directory.
   - Add the following environment variable:
     ```
     MONGODB_URI=<your_mongodb_connection_uri>
     ```

4. Start the server:
   ```bash
   uvicorn main:app  --host 127.0.0.1 --port 8080
   ```

5. The API is now available at `http://localhost:8080/`. You can use tools like Postman or curl to interact with the API.

## API Endpoints

The following API endpoints are available:

- `POST /api/students`: Create a new student record.
- `GET /api/students`: List student records with optional filtering by country and age.
- `GET /api/students/{id}`: Retrieve a specific student record.
- `PATCH /api/students/{id}`: Update a specific student record.
- `DELETE /api/students/{id}`: Delete a specific student record.

Please refer to the docstrings and the response schemas in the `student.py` file for more details on the API endpoints.

---
