import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(100)
y = np.random.randn(100)

colors = np.random.rand(100)
sizes = np.abs(np.random.randn(100))*100
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')

#信息备注
cbar = plt.colorbar(scatter)
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()
plt.show()