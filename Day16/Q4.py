import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

temp_series = pd.Series(temps)

plt.figure(figsize=(8, 5))
plt.plot(temp_series, marker='o')

plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.grid(True)

plt.show()