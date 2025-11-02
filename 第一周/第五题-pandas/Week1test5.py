import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_path = r"C:\Users\Luchenghao\Desktop\Turing_AI_week_one\第一周\第五题-pandas\附件.xlsx"
df = pd.read_excel(file_path)

fleets = df['车队编码'].unique()

for fleet in fleets:
    data = df[df['车队编码'] == fleet]

    plt.figure(figsize = (10,6))
    plt.scatter(data['在途时长'], data['自有变动成本'])
    plt.scatter(data['在途时长'], data['外部承运商成本'])

    plt.title(f"{fleet}运行成本散点图")
    plt.xlabel("在途时长")
    plt.ylabel("成本")
    plt.legend()
    plt.grid(True)
    plt.show()

for fleet in fleets:
    data = df[df['车队编码'] == fleet][['在途时长', '自有变动成本', '外部承运商成本']]
    print(f"\n{fleet}")
    print(data.describe().loc[['max', 'min', 'mean', '50%']])

print("\n各队最佳成本")
each_best = {}
for fleet in fleets:
    data = df[df['车队编码'] == fleet]
    total = data['自有变动成本'] + data['外部承运商成本']
    aver = total / data['在途时长']
    each_best[fleet] = aver.min()
    print(f"\n{fleet}")
    print(each_best[fleet])

plt.figure(figsize=(8, 5))
plt.bar(each_best.keys(), each_best.values())
plt.title("各车队最佳时均成本对比")
plt.xlabel("车队")
plt.ylabel("最佳时均成本")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()


