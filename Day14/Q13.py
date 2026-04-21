import numpy as np
import pandas as pd
arr = np.array([10, 25, 30, 15, 40])
series = pd.Series(arr)
filtered_series = series[series > 20]
print(filtered_series)