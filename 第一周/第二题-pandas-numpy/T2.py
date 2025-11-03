import numpy as np
import pandas as pd

df1 = np.random.rand(5, 5)
df1 = pd.DataFrame(df1, columns=['a', 'b', 'c', 'd', 'e'])
print(df1)
c = df1.sum()
i = c.idxmin()
print(i)