import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 400)
y = np.sin(x)
plt.plot(x, y, '--')
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('三角函数')
plt.legend(['sinx'])
plt.show()