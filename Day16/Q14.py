import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)

plt.figure(figsize=(14, 10))

plt.subplot(2, 3, 1)
plt.plot(df["Day"], df["Temperature"], marker='o', color='blue')
plt.title("Daily Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.bar(df["Day"], df["Temperature"], color='orange')
plt.title("Day-wise Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")

plt.subplot(2, 3, 3)
high = (df["Temperature"] > 30).sum()
low = (df["Temperature"] <= 30).sum()

plt.pie([high, low],
        labels=["High (>30°C)", "Low (≤30°C)"],
        autopct='%1.1f%%',
        colors=["red", "skyblue"])
plt.title("High vs Low Temperature")

plt.subplot(2, 3, 4)
plt.hist(df["Temperature"], bins=5, color='purple', edgecolor='black')
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

plt.subplot(2, 3, 5)
plt.scatter(range(len(df["Day"])), df["Temperature"], color='green')
plt.xticks(range(len(df["Day"])), df["Day"])
plt.title("Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.tight_layout()
plt.show()