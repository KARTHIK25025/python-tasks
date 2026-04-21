import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

plt.figure(figsize=(18, 10))

plt.subplot(2, 3, 1)
plt.plot(df["Student"], df["Marks"], marker='o', color='blue')
plt.title("Marks Trend (Line Graph)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.bar(df["Student"], df["Marks"], color='orange')
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(axis='y')

pass_count = (df["Marks"] > 50).sum()
fail_count = (df["Marks"] <= 50).sum()

plt.subplot(2, 3, 3)
plt.pie([pass_count, fail_count],
        labels=["Pass", "Fail"],
        autopct='%1.1f%%',
        colors=['green', 'red'],
        startangle=90)
plt.title("Pass vs Fail")
plt.axis('equal')

plt.subplot(2, 3, 4)
plt.hist(df["Marks"], bins=5, color='purple', edgecolor='black')
plt.title("Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")
plt.grid(axis='y')

plt.subplot(2, 3, 5)
plt.scatter(df.index, df["Marks"], color='brown')
plt.title("Index vs Marks (Scatter Plot)")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.grid(True)

plt.tight_layout()

plt.show()