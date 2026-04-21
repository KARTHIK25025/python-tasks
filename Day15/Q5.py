class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"
employees = {}
n = int(input("Enter number of employees: "))
for i in range(n):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    while True:
        try:
            salary = float(input("Enter Salary: "))
            if salary < 0:
                print("Salary cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    emp = Employee(emp_id, name, salary)
    employees[emp_id] = emp
try:
    with open("employees.txt", "w") as file:
        for emp in employees.values():
            file.write(emp.display() + "\n")
    print("\nEmployee data saved to file.")
except Exception as e:
    print("Error while writing to file:", e)
print("\nEmployee Details:")
for emp in employees.values():
    print(emp.display())