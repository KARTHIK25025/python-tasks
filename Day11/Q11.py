import numpy as np
temps = np.array([28, 31, 35, 27, 40, 22])
filtered_temps = temps[temps > 30]
print("Temperatures above 30°C:", filtered_temps)