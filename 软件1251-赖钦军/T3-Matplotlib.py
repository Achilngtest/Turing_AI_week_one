import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0,10)
y = np.sin(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, c='b', linestyle='--', label='sin(x)')

plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)

ax = plt.gca()

ax.set_title('三角函数', fontsize=20, c='black')

plt.legend()

plt.show()