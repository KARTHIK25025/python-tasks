import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(df["Product"], df["Sales"], marker='o', color='blue')
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(True)

plt.subplot(1, 3, 2)
plt.bar(df["Product"], df["Sales"], color='orange')
plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(axis='y')

plt.subplot(1, 3, 3)
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution")
plt.axis('equal')

plt.tight_layout()

plt.show()