name = input("Enter student name: ")

with open("attendance.txt", "a") as file:
    file.write(name + "\n")

with open("attendance.txt", "r") as file:
    print("\nAttendance Record:")
    print(file.read())
