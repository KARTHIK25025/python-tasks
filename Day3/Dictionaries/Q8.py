student_marks = {
    "Phani": 85,
    "Karthik": 92,
    "Anand": 78,
    "Varun": 95,
}
top_student = max(student_marks, key=student_marks.get)
print(f"The top student is {top_student} with {student_marks[top_student]} marks.")
