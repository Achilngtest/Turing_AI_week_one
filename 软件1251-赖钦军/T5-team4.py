import pandas as pd
import plotly.express as px

data = pd.read_excel("C:\\Users\JackieLai\PycharmProjects\Turing_AI_W1\附件.xlsx",
                         engine='openpyxl')

# 切分车队数据
data_team4 = data.iloc[198:240]
# 按column分割
time4 = data_team4[['在途时长']].values.flatten().reshape(-1)
print("车队4在途时长最大值：", time4.max())
print("车队4在途时长最小值：", time4.min())
print(f"车队4在途时长平均值：{time4.mean():.2f}")
print("车队4在途时长中位数：", np.median(time4))

own_cost4 = data_team4[['自有变动成本']].values.flatten().reshape(-1)
print("车队4自有变动成本最大值：", own_cost4.max())
print("车队4自有变动成本最小值：", own_cost4.min())
print(f"车队4自有变动成本平均值：{own_cost4.mean():.2f}")
print("车队4自有变动成本中位数：", np.median(own_cost4))

ex_cost4 = data_team4[['外部承运商成本']].values.flatten().reshape(-1)
print("车队4外部承运商成本最大值：", ex_cost4.max())
print("车队4外部承运商成本最小值：", ex_cost4.min())
print(f"车队4外部承运商成本平均值：{ex_cost4.mean():.2f}")
print("车队4外部承运商成本中位数：", np.median(ex_cost4))

df = pd.DataFrame({'在途时长': time4, '自有变动成本': own_cost4, '外部承运商成本': ex_cost4})

fig = px.scatter_3d(
    df, x="在途时长", y="自有变动成本", z="外部承运商成本",
    color="自有变动成本",
    size='外部承运商成本',
    title='车队4：在途时长、自有变动成本、外部承运商成本3D散点图'
)

fig.update_layout(scene=dict(xaxis_title='在途时长', yaxis_title='自有变动成本', zaxis_title='外部承运商成本',))
fig.show()