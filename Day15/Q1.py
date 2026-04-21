import math
students = [
    ("Anand", 67),
    ("Babu", 45),
    ("Karthik", 82),
    ("vamsi", 39),
    ("dheeraj", 55)
]
student_dict = dict(students)
above_50 = []
total_marks = 0
for name, marks in student_dict.items():
    total_marks += marks
    if marks > 50:
        above_50.append(name)
average = total_marks / len(student_dict)
average = math.floor(average)
with open("student_results.txt", "w") as file:
    file.write("Student Dictionary:\n")
    file.write(str(student_dict) + "\n\n")
    file.write("Students scoring above 50:\n")
    for student in above_50:
        file.write(student + "\n")
    file.write("\nAverage Marks: " + str(average))
print("Processing complete. Results saved to 'student_results.txt'")