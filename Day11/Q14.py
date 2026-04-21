import numpy as np
scores = np.array([50, 60, 70, 80, 90, 100, 110, 120])
parts = np.array_split(scores, 4)
for i, part in enumerate(parts):
    print(f"Server {i+1}:", part)