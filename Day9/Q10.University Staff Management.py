class Staff:
    def __init__(self, name, department):
        self.name = name
        self.department = department
class Professor(Staff):
    def display(self):
        print(f"Professor: {self.name} | Dept: {self.department}")
class LabAssistant(Staff):
    def display(self):
        print(f"Lab Assistant: {self.name} | Dept: {self.department}")
class Administrator(Staff):
    def display(self):
        print(f"Administrator: {self.name} | Dept: {self.department}")
prof = Professor("Dr. Bharat", "Computer Science")
lab_tech = LabAssistant("Rameshn", "Physics")
admin = Administrator("Sarath", "Admissions")
prof.display()
lab_tech.display()
admin.display()
