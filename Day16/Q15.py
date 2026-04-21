import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.plot(df["Product"], df["Sales"], marker='o', color='blue')
plt.title("Sales Trend")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.bar(df["Product"], df["Sales"], color='green')
plt.title("Product vs Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.subplot(2, 3, 3)
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%')
plt.title("Sales Contribution")

plt.subplot(2, 3, 4)
plt.hist(df["Profit"], bins=5, color='orange', edgecolor='black')
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.subplot(2, 3, 5)
plt.scatter(df["Sales"], df["Profit"], color='red')
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)

plt.tight_layout()
plt.show()