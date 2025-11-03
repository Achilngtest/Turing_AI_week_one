import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.linspace(0, 10, 50)
y = np.sin(x)

plt.figure()
plt.plot(x, y,linestyle='--' , label='sin(x)')

plt.xlim((0, 10))
plt.ylim((-1.5, 1.5))
plt.title('三角函数')
plt.legend()

plt.show()