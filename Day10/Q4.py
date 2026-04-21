import numpy as np

sensor1 = [10, 20, 30]
sensor2 = [40, 50, 60]

array1 = np.array(sensor1)
array2 = np.array(sensor2)

combined_array = np.concatenate((array1, array2))

print("Combined Sensor Readings:", combined_array)