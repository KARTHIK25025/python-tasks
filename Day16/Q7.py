import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

filtered_df = df[df["Marks"] > 50]

plt.figure(figsize=(8, 5))
plt.bar(filtered_df["Name"], filtered_df["Marks"], color='green')

plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Students with Marks > 50")

plt.grid(axis='y')

plt.show()