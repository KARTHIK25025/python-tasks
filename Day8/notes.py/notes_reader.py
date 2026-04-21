with open("notes.txt", "w") as file:
    file.write("Today I studied Python\nFile handling is easy")
 
def read_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            print("\nYour Notes:")
            print(content)
    except FileNotFoundError:
        print("notes.txt file not found.")
 
read_notes()
