import numpy as np
matrix = np.random.randint(0, 51, (3, 3))
filtered = matrix[matrix > 25]
print("Matrix:\n", matrix)
print("Filtered values (>25):", filtered)