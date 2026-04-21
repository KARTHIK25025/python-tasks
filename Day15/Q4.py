while True:
    try:
        log_entry = input("Enter log message (or type 'exit' to stop): ")
        if log_entry.lower() == "exit":
            print("Logging stopped.")
            break
        with open("log.txt", "a") as file:
            file.write(log_entry + "\n")
        print("Log saved successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print("Unexpected error:", e)