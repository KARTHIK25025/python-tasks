import numpy as np
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
unique_vals, counts = np.unique(data, return_counts=True)
print("Values:", unique_vals)
print("Counts:", counts)