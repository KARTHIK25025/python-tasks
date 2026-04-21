def apply_bonus(func):
    def wrapper(self):
        bonus = self.salary * 0.10
        total_salary = self.salary + bonus
        print(f"Base Salary: Rupees {self.salary} | Bonus Added: Rupees {bonus}")
        return func(self, total_salary)
    return wrapper
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @apply_bonus
    def display_salary(self, total_salary=None):
        print(f"Employee: {self.name} | Total Compensation: Rupees {total_salary}")
emp = Employee("Karthik", 60000)
emp.display_salary()
