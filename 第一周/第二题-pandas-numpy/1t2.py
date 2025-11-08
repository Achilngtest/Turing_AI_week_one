import numpy as np
import pandas as pd
s=np.random.rand(5,5)
df=pd.DataFrame(s,columns=['a','b','c','d','e'])
print(df)
s_sum=df.sum()
print(s_sum.idxmin())