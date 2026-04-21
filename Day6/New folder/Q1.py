subjects = ("Math", "Science", "English")
student_names = set()
student_records = {}

def calculate_total_recursive(marks):
    """Recursive function to calculate the total marks."""
    if not marks:
        return 0
    
    try:
        return marks[0] + calculate_total_recursive(marks[1:])
    except TypeError:
        raise TypeError("Marks data type error.")

def add_student():
    """Function to add a new student and their marks."""
    name = input("Enter student name: ")
    marks = []
    
    try:
        for subject in subjects:
            mark = int(input(f"Enter marks for {subject}: "))
            marks.append(mark)
            
        student_names.add(name)
        student_records[name] = marks
        
    except ValueError:
        print("Invalid input! Please enter numeric marks.")

def display_students():
    """Function to display all student records."""
    if not student_records:
        print("No student records found.")
        return
        
    for name, marks in student_records.items():
        print(f"{name} : {marks}")

def calculate_average():
    """Function to calculate and display the total and average marks of a student."""
    try:
        name = input("Enter student name to calculate average: ")
        
        if name not in student_names:
            raise NameError("Student name not found.")
        
        marks = student_records[name]
        
        if len(marks) == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
            
        total = calculate_total_recursive(marks)
        average = total / len(marks)
        
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average}")
        
    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Marks data type error.")

def main():
    """Main menu-driven loop."""
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
