import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Store_A"], marker='o', label="Store A")
plt.plot(df["Month"], df["Store_B"], marker='s', label="Store B")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Comparison: Store A vs Store B")

plt.legend()

plt.grid(True)

plt.show()