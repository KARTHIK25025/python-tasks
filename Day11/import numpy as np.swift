 import numpy as np
codes = [2, 4, 1, 4, 3, 4, 5]
arr = np.array(codes)
indexes = np.where(arr == 4)
print("Indexes where value is 4:", indexes[0])