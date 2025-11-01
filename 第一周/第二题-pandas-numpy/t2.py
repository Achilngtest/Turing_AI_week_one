import numpy as np
import pandas as pd

arr = np.random.rand(5, 5)
df = pd.DataFrame(arr, columns=list('abcde'))
print(df)
print(str(df.sum().idxmin()))
