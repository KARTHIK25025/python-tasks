import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

print(df)

plt.figure(figsize=(14, 10))

plt.subplot(2, 3, 1)
plt.plot(df["Salary"], marker='o', color='blue')
plt.title("Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.bar(df["Department"], df["Salary"], color='orange')
plt.title("Department-wise Salary Comparison")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.subplot(2, 3, 3)
dept_counts = df["Department"].value_counts()
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Department Distribution")

plt.subplot(2, 3, 4)
plt.hist(df["Salary"], bins=5, color='purple', edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary Range")
plt.ylabel("Frequency")

plt.subplot(2, 3, 5)
plt.scatter(range(len(df["Salary"])), df["Salary"], color='red')
plt.title("Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.grid(True)

plt.tight_layout()
plt.show()