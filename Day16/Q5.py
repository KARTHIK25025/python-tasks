import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Sales"], color='orange')

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Bar Chart")

plt.grid(axis='y')

plt.show()