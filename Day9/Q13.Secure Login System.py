is_logged_in = False
def login_required(func):
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            print("Access Denied: Please log in first.")
            return
        return func(*args, **kwargs)
    return wrapper
@login_required
def view_dashboard():
    print("Welcome to your secure dashboard!")
view_dashboard()
is_logged_in = True
view_dashboard()
