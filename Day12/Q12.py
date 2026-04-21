import numpy as np
data = np.random.rand(8)
normalized = data * 100
filtered = normalized[normalized > 50]
sorted_values = np.sort(filtered)
print("Original data:", data)
print("Normalized data:", normalized)
print("Filtered (>50):", filtered)
print("Sorted filtered values:", sorted_values)