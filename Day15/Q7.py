import os
 
def read_logs(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
 
 
def create_log_file(file_path):
    if not os.path.exists(file_path):
        print("log.txt not found. Creating sample log file...")
        with open(file_path, 'w') as f:
            f.write("""INFO: System started
ERROR: Disk not found
WARNING: Low memory
ERROR: File missing
INFO: Process running
ERROR: Disk not found
""")
 
 
def process_logs(file_path):
    create_log_file(file_path)
 
    error_count = {}  # dictionary to count errors
 
    # Loop through logs using generator
    for line in read_logs(file_path):
 
        # Condition to filter only ERROR logs
        if "ERROR" in line:
            error_msg = line.split("ERROR:")[-1].strip()
 
            # Count occurrences using dictionary
            if error_msg in error_count:
                error_count[error_msg] += 1
            else:
                error_count[error_msg] = 1
 
    return error_count
 
if __name__ == "__main__":
    file_path = "log.txt"
 
    result = process_logs(file_path)
 
    print("\nError Summary:\n")
    for error, count in result.items():
        print(f"{error} : {count}")
 
import os
 
def read_logs(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
 
 
def create_log_file(file_path):
    if not os.path.exists(file_path):
        print("log.txt not found. Creating sample log file...")
        with open(file_path, 'w') as f:
            f.write("""INFO: System started
ERROR: Disk not found
WARNING: Low memory
ERROR: File missing
INFO: Process running
ERROR: Disk not found
""")
 
 
def process_logs(file_path):
    create_log_file(file_path)
 
    error_count = {}  # dictionary to count errors
 
    # Loop through logs using generator
    for line in read_logs(file_path):
 
        # Condition to filter only ERROR logs
        if "ERROR" in line:
            error_msg = line.split("ERROR:")[-1].strip()
 
            # Count occurrences using dictionary
            if error_msg in error_count:
                error_count[error_msg] += 1
            else:
                error_count[error_msg] = 1
 
    return error_count
 
if __name__ == "__main__":
    file_path = "log.txt"
 
    result = process_logs(file_path)
 
    print("\nError Summary:\n")
    for error, count in result.items():
        print(f"{error} : {count}")
 