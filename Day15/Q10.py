import random
import numpy as np
import pandas as pd
import math
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()
    def assign_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"
    def display(self):
        return f"{self.name} - {self.marks} - {self.grade}"
try:
    n = int(input("Enter number of students: "))
    marks_list = [random.randint(0, 100) for _ in range(n)]
    marks_array = np.array(marks_list)
    students = []
    for i in range(n):
        student = Student(f"Student_{i+1}", marks_array[i])
        students.append(student)
    data = {
        "Name": [s.name for s in students],
        "Marks": [s.marks for s in students],
        "Grade": [s.grade for s in students]
    }
    df = pd.DataFrame(data)
    avg = sum(marks_array) / len(marks_array)
    avg = math.floor(avg)
    with open("report.txt", "w") as file:
        file.write("Student Report\n\n")
        file.write(df.to_string(index=False))
        file.write(f"\n\nAverage Marks: {avg}")
    print("\nStudent Results:")
    for s in students:
        print(s.display())
    print("\nDataFrame:\n")
    print(df)
    print("\nAverage Marks:", avg)
    print("\nReport saved to 'report.txt'")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except Exception as e:
    print("An error occurred:", e)