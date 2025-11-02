import numpy as np
import pandas as pd

arr = np.random.rand(5, 5)
df = pd.DataFrame(arr, columns=['a', 'b', 'c', 'd', 'e'])
print(df)

sums = df.sum()
min = sums.idxmin()
print(sums)
print("\n列和最小的是:")
print(min)