# ===============================================================================================
# Student Management System
# ===============================================================================================
 
# Importing necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
 
# Creating an instance of FastAPI
app = FastAPI()
 
# Temporary in-memory database
students = []
 
# Defining a Pydantic model for Student
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: float
 
 
# Creating an API endpoint to add a student
@app.post("/students/")
def add_student(student: Student):
 
    # Check if student already exists
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")
 
    students.append(student)
 
    return {
        "message": "Student added successfully",
        "student": student
    }
 
 
# Creating an API endpoint to fetch all student records
@app.get("/students/", response_model=List[Student])
def get_students():
    return students
 
 
# Creating an API endpoint to fetch a student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
 
    for student in students:
        if student.id == student_id:
            return student
 
    raise HTTPException(status_code=404, detail="Student not found")
 
 
# Creating an API endpoint to update a student record
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
 
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
 
            return {
                "message": "Student updated successfully",
                "student": updated_student
            }
 
    raise HTTPException(status_code=404, detail="Student not found")
 
 
# Creating an API endpoint to delete a student record
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
 
    for index, student in enumerate(students):
        if student.id == student_id:
 
            deleted_student = students.pop(index)
 
            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }
 
    raise HTTPException(status_code=404, detail="Student not found")