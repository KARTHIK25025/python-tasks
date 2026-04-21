import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)

plt.figure(figsize=(14, 10))

plt.subplot(2, 3, 1)
plt.plot(df["Month"], df["Sales"], marker='o', color='blue')
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.bar(df["Month"], df["Sales"], color='orange')
plt.title("Month-wise Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.subplot(2, 3, 3)
plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%', startangle=90)
plt.title("Sales Contribution")

plt.subplot(2, 3, 4)
plt.hist(df["Sales"], bins=5, color='purple', edgecolor='black')
plt.title("Sales Frequency")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.subplot(2, 3, 5)
plt.scatter(range(len(df["Month"])), df["Sales"], color='red')
plt.xticks(range(len(df["Month"])), df["Month"])
plt.title("Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()