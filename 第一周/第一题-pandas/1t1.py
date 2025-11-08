import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame: # 传入类型为pd.DataFrame的参数df1、df2，要求返回值类型为pd.DataFrame
    # 你的代码

    result = pd.concat([df1, df2], ignore_index=True)
    return result# 返回值


