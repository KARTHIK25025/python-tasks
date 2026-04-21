import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"], color='skyblue')

plt.xlabel("Student Names")
plt.ylabel("Marks")

plt.title("Student Marks Bar Chart")

plt.grid(axis='y')

plt.show()