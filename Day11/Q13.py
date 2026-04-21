import numpy as np
arr = np.array([10, 20, 30, 40])
copy_arr = arr.copy()
arr[0] = 999
print("After modifying original (COPY):")
print("Original:", arr)
print("Copy:    ", copy_arr)
arr2 = np.array([10, 20, 30, 40])
view_arr = arr2.view()
arr2[1] = 888
print("\nAfter modifying original (VIEW):")
print("Original:", arr2)
print("View:    ", view_arr)