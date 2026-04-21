import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

series = pd.Series(data)

mean_value = series.mean()
cleaned_series = series.fillna(mean_value)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(cleaned_series, marker='o', color='blue')
plt.title("Line Graph - Cleaned Data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)

avg_value = cleaned_series.mean()
filtered = cleaned_series[cleaned_series > avg_value]

plt.subplot(1, 2, 2)
plt.bar(filtered.index, filtered.values, color='green')
plt.title("Values Greater Than Average")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(axis='y')

plt.tight_layout()

plt.show()