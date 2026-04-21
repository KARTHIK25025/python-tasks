with open("marks.txt", "w") as file:
    file.write("Rahul 80\nAnita 90\nRavi 75")
def analyze_marks():
    total = 0
    count = 0
 
    try:
        with open("marks.txt", "r") as file:
            for line in file:
                name, marks = line.split()
                marks = int(marks)
 
                print(name, marks)
 
                total += marks
                count += 1
 
        average = total / count
        print("Average Marks:", average)
 
    except FileNotFoundError:
        print("File not found")
 
analyze_marks()
import os
print(os.getcwd())
