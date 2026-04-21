users = {
    "Karthik": "admin",
    "Anand": "user",
    "Phani": "guest"
}
current_user = "Karthik"
def require_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_role = users.get(current_user)
            if user_role == required_role:
                return func(*args, **kwargs)
            else:
                print(f"Access denied for {current_user}! Required role: {required_role}")
        return wrapper
    return decorator
@require_role("admin")
def delete_data():
    print("Data deleted successfully.")
@require_role("user")
def view_data():
    print("Data viewed successfully.")
@require_role("admin")
def modify_data():
    print("Data modified successfully.")
print("Current User:", current_user)
delete_data()
view_data()
modify_data()