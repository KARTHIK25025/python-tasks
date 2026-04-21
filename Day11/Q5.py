import numpy as np
marks = [
    [78, 85],
    [90, 88],
    [67, 72]
]
arr = np.array(marks)
value = arr[1, 1]
print("Second student's second subject mark:", value)