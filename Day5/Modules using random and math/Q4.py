import random
import math
numbers = [random.randint(1, 200) for _ in range(20)]
print(f"Generated list:\n{numbers}\n")
max_val = max(numbers)
min_val = min(numbers)
sqrt_max = math.sqrt(max_val)
log_min = math.log(min_val)
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
print(f"Square root of the maximum number: {sqrt_max:.2f}")
print(f"Logarithm of the minimum number: {log_min:.2f}")
