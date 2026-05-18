# ============================================================
# 📝 FastAPI Student Management System App - MongoDB Atlas
# ============================================================
# Install:
# pip install fastapi uvicorn mongoengine pymongo dnspython
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import (
    connect,
    Document,
    IntField,
    StringField,
    BooleanField
)

# ============================================================
# 🚀 Create FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🌐 MongoDB Atlas Connection
# ============================================================

MONGO_URL = "mongodb+srv://venkat:venkat123@cluster0.pspvie7.mongodb.net/?retryWrites=true&w=majority"

connect(
    db="student_db",
    host=MONGO_URL
)

# ============================================================
# 🧱 MongoDB Model
# ============================================================

class Studentdb(Document):

    id = IntField(primary_key=True)

    name = StringField(
        required=True,
        max_length=100
    )

    age = IntField(required=True)

    marks = IntField(required=True)

    course = StringField(
        required=True,
        max_length=100
    )

    is_active = BooleanField(default=True)

    meta = {
        "collection": "students",
        "ordering": ["id"]
    }

# ============================================================
# 🧾 Pydantic Schemas
# ============================================================

class Student(BaseModel):

    id: int
    name: str
    age: int
    marks: int
    course: str
    is_active: bool = True

# ============================================================
# 🏠 Home Route
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI + MongoDB Student Management System 🚀"
    }

# ============================================================
# ✅ 1. CREATE STUDENT
# ============================================================

@app.post("/students")
def create_student(student: Student):

    # Check duplicate ID
    existing_student = Studentdb.objects(
        id=student.id
    ).first()

    if existing_student:

        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    # Create student
    new_student = Studentdb(
        id=student.id,
        name=student.name,
        age=student.age,
        marks=student.marks,
        course=student.course,
        is_active=student.is_active
    )

    new_student.save()

    return {
        "message": "Student created successfully",
        "data": {
            "id": new_student.id,
            "name": new_student.name,
            "age": new_student.age,
            "marks": new_student.marks,
            "course": new_student.course,
            "is_active": new_student.is_active
        }
    }

# ============================================================
# ✅ 2. GET ALL STUDENTS
# ============================================================

@app.get("/students")
def get_all_students():

    students = Studentdb.objects()

    data = []

    for student in students:

        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "marks": student.marks,
            "course": student.course,
            "is_active": student.is_active
        })

    return {
        "count": len(data),
        "students": data
    }

# ============================================================
# ✅ 3. GET STUDENT BY ID
# ============================================================

@app.get("/students/{student_id}")
def get_student(student_id: int):

    student = Studentdb.objects(
        id=student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "marks": student.marks,
        "course": student.course,
        "is_active": student.is_active
    }

# ============================================================
# ✅ 4. UPDATE STUDENT
# ============================================================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student
):

    student = Studentdb.objects(
        id=student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Update fields
    student.name = updated_student.name
    student.age = updated_student.age
    student.marks = updated_student.marks
    student.course = updated_student.course
    student.is_active = updated_student.is_active

    student.save()

    return {
        "message": "Student updated successfully"
    }

# ============================================================
# ✅ 5. DELETE STUDENT
# ============================================================

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    student = Studentdb.objects(
        id=student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.delete()

    return {
        "message": "Student deleted successfully"
    }