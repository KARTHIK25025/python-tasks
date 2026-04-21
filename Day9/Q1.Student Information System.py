class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def display(self):
        print(f"Student: {self.name} | Roll No: {self.roll_number} | Marks: {self.marks}")
s1 = Student("Karthik", 101, 88)
s2 = Student("Phani", 102, 92)
s3 = Student("Anand", 103, 79)
s1.display()
s2.display()
s3.display()
