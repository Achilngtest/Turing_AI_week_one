import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 中文环境
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '附件.xlsx')
df = pd.read_excel(DATA_DIR)

# 按车队编码分组
g = df.groupby('车队编码')

# 五张散点图
_, x = plt.subplots(1, 5, figsize=(25, 5))
for (name, data), ax in zip(g, x):
    ax.scatter(data['在途时长'], data['自有变动成本'],
               label='自有变动成本')
    ax.scatter(data['在途时长'], data['外部承运商成本'],
               label='外部承运商成本')

    ax.set_title(name)
    ax.set_xlabel('在途时长')
    ax.set_ylabel('成本')

    ax.legend()
    ax.grid(True)
    
# 回执
plt.suptitle('各车队成本与在途时长散点图', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# 统计信息
for name, data in g:
    
    print(f"\n车队编码：{name}")
    print(f"在途时长：最大值={data['在途时长'].max():.2f}, "
      f"最小值={data['在途时长'].min():.2f}, "
      f"平均值={data['在途时长'].mean():.2f}, "
      f"中位数={data['在途时长'].median():.2f}")

    print(f"自有变动成本：最大值={data['自有变动成本'].max():.2f}, "
      f"最小值={data['自有变动成本'].min():.2f}, "
      f"平均值={data['自有变动成本'].mean():.2f}, "
      f"中位数={data['自有变动成本'].median():.2f}")

    print(f"外部承运商成本：最大值={data['外部承运商成本'].max():.2f}, "
      f"最小值={data['外部承运商成本'].min():.2f}, "
      f"平均值={data['外部承运商成本'].mean():.2f}, "
      f"中位数={data['外部承运商成本'].median():.2f}")


# 算成本
df['时均成本'] = (df['自有变动成本'] + df['外部承运商成本']) / df['在途时长']
best = g['时均成本'].mean()

print("\n最佳时均成本：")
print(best)

# 柱状图
best.plot(kind='bar', figsize=(8, 5), title='最佳时均成本',
          xlabel='车队编码', ylabel='时均成本', grid=True)
plt.show()
