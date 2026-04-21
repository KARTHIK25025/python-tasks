import numpy as np
import pandas as pd
import math
marks = np.random.randint(0, 101, 10)
students = [f"Student_{i+1}" for i in range(10)]
df = pd.DataFrame({
    "Name": students,
    "Marks": marks
})
print("All Student Data:\n")
print(df)
passing_students = df[df["Marks"] >= 50]
print("\nPassing Students:\n")
print(passing_students)
mean_marks = np.mean(df["Marks"])
mean_marks = math.floor(mean_marks)
print("\nAverage Marks:", mean_marks)
print("\nDetailed Results:")
for index, row in df.iterrows():
    status = "Pass" if row["Marks"] >= 50 else "Fail"
    print(f"{row['Name']} - {row['Marks']} ({status})")