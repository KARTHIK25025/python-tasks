import time
def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[{func.__name__}] executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper
@track_time
def slow_function():
    time.sleep(1)
    print("Task finished.")
slow_function()
