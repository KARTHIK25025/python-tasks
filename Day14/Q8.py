import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})
df["Status"] = np.where(df["Marks"] < 50, "Fail", "Pass")
passed_students = df[df["Status"] == "Pass"]
avg_marks = passed_students["Marks"].mean()
print(df)
print("\nPassed Students:")
print(passed_students)
print("\nAverage Marks of Passed Students:", avg_marks)