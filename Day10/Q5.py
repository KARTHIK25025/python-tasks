import numpy as np

store_a = [200, 250, 300]
store_b = [180, 270, 310]

array_a = np.array(store_a)
array_b = np.array(store_b)

difference = array_a - array_b

print("Daily Sales Difference:", difference)