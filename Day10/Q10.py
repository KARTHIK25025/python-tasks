import numpy as np

data = np.array([12, 7, 25, 3, 18, 10])

sorted_arr = np.sort(data)

split_arrays = np.array_split(sorted_arr, 2)

sum_part1 = np.sum(split_arrays[0])
sum_part2 = np.sum(split_arrays[1])

print("Sorted Array:", sorted_arr)
print("Split Array 1:", split_arrays[0])
print("Split Array 2:", split_arrays[1])
print("Sum of Part 1:", sum_part1)
print("Sum of Part 2:", sum_part2)