import numpy as np
import pandas as pd
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})
filtered_df = df[df["Marks"] > 75]
print(df)
print("\nFiltered DataFrame:\n", filtered_df)