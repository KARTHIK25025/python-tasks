import numpy as np
import pandas as pd
arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])
df = pd.DataFrame(arr, columns=["Sales", "Profit"])
filtered_df = df[df["Sales"] > 100]
avg_profit = filtered_df["Profit"].mean()
print(df)
print("\nFiltered DataFrame:\n", filtered_df)
print("\nAverage Profit:", avg_profit)