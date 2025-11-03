import pandas as pd
import os

if len(os.listdir('excel_data'))>0:
    df_1 = pd.read_excel('excel_data/001.xlsx')
    df_2 = pd.read_excel('excel_data/002.xlsx')
else:
    df_1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df_2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
def concatenate_tables(df1, df2): # 传入类型为pd.DataFrame的参数df1、df2，要求返回值类型为pd.DataFrame
    result = pd.merge(df1, df2, how='outer') # 合并两个表格
    return result # 返回值
result_1 = concatenate_tables(df_1, df_2)
print(result_1)
