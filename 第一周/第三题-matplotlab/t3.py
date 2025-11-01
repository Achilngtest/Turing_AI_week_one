import numpy as np
import matplotlib.pyplot as plt

# 中文依旧最大bug来源
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def show(x, y):
    # 画出来，带图例那种
    plt.plot(x, y, linestyle='--', label='sin(x)')
    plt.grid(True)
    # 范围
    plt.xlim(0, 10)
    plt.ylim(-1.5, 1.5)
    # 标签
    plt.xlabel('x')
    plt.ylabel('y')
    # 标题
    plt.title('三角函数')
    # 网格
    plt.legend()

    plt.show()


x = np.linspace(0, 10, 500)
y = np.sin(x)

show(x, y)
