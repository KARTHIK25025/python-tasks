import numpy as np

data = [5, 10, 15, 20, 25, 30]

data_array = np.array(data)

split_data = np.array_split(data_array, 3)

print("Split Data:")
for i, part in enumerate(split_data, 1):
    print(f"Part {i}:", part)