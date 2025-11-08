import pandas as pd
import plotly.express as px

data = pd.read_excel("C:\\Users\JackieLai\PycharmProjects\Turing_AI_W1\附件.xlsx",
                         engine='openpyxl')

# 切分车队数据
data_team2 = data.iloc[72:110]

# 按column分割
time2 = data_team2[['在途时长']].values.flatten().reshape(-1)
print("车队2在途时长最大值：", time2.max())
print("车队2在途时长最小值：", time2.min())
print(f"车队2在途时长平均值：{time2.mean():.2f}")
print("车队2在途时长中位数：", np.median(time2))

own_cost2 = data_team2[['自有变动成本']].values.flatten().reshape(-1)
print("车队2自有变动成本最大值：", own_cost2.max())
print("车队2自有变动成本最小值：", own_cost2.min())
print(f"车队2自有变动成本平均值：{own_cost2.mean():.2f}")
print("车队2自有变动成本中位数：", np.median(own_cost2))

ex_cost2 = data_team2[['外部承运商成本']].values.flatten().reshape(-1)
print("车队2外部承运商成本最大值：", ex_cost2.max())
print("车队2外部承运商成本最小值：", ex_cost2.min())
print(f"车队2外部承运商成本平均值：{ex_cost2.mean():.2f}")
print("车队2外部承运商成本中位数：", np.median(ex_cost2))

df = pd.DataFrame({'在途时长': time2, '自有变动成本': own_cost2, '外部承运商成本': ex_cost2})

fig = px.scatter_3d(
    df, x="在途时长", y="自有变动成本", z="外部承运商成本",
    color="自有变动成本",
    size='外部承运商成本',
    title='车队2：在途时长、自有变动成本、外部承运商成本3D散点图'
)

fig.update_layout(scene=dict(xaxis_title='在途时长', yaxis_title='自有变动成本', zaxis_title='外部承运商成本',))
fig.show()