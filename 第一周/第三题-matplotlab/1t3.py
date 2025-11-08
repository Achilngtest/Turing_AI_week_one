import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.show()
