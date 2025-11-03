import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('附件.xlsx')
r = set(df.loc[:,'车队编码'])

h = df.columns.tolist()[1:]
v = []
for i in r:
    c = []
    df1 = df.loc[df['车队编码'] == f'{i}']
    df1 = df1.drop(columns='车队编码')
    x = df1.loc[:,'在途时长']
    y = df1.loc[:,'自有变动成本']
    y1 = df1.loc[:,'外部承运商成本']
    plt.scatter(x, y,label='自有变动成本')
    plt.scatter(x, y1,label='外部承运商成本')
    plt.legend()
    plt.show()
    for j in range(len(x)):
        c.append((list(y)[j]+list(y1)[j])/list(x)[j])
    print(f'{i}:{min(c)}')
    v.append(min(c))
plt.bar(list(r),v)
plt.show()

