import numpy as np

scores = np.array([85, 92, 78, 95, 88, 62, 74, 91])

print(scores[scores >= 80])  # [85 92 95 88 91]

print(scores[(scores >= 75) & (scores < 90)])  # [85 78 88]

