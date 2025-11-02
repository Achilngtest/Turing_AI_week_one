import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.randn(100)
sizes = np.random.randn(100) * 1000

scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis', marker='o')
plt.colorbar(scatter)
plt.show()