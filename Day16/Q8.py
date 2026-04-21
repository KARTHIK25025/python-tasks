import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

score_series = pd.Series(scores)

pass_count = (score_series > 50).sum()
fail_count = (score_series <= 50).sum()

labels = ["Pass", "Fail"]
counts = [pass_count, fail_count]

plt.figure(figsize=(6, 6))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['green', 'red'])

plt.title("Pass vs Fail Distribution")

plt.axis('equal')

plt.show()