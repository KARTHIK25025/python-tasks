class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def display_details(self):
        print(f"Manager Name: {self.name} | Salary: Rupees {self.salary}")
mgr = Manager("Karthik", 76000)
mgr.display_details()
