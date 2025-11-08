"""
使用pandas、NumPy请完成如下任务：

1. 生成一个 5×5 的随机浮点数数组，元素取自区间 ([0,1))。
2. 将其转换为一个 `pandas.DataFrame`，列名依次为 `a, b, c, d, e`。
3. 将该表完整打印到控制台。
4. 计算每一列的列和，并输出“列和最小”的那一列的列名（字符串形式）。
"""

import pandas as pd
import numpy as np

rand_arr = np.random.rand(5, 5)
df_arr = pd.DataFrame(rand_arr, columns=['a', 'b', 'c', 'd', 'e'])
print(df_arr)
print()
sum_arr = df_arr.sum()
print(str(sum_arr.idxmax()))