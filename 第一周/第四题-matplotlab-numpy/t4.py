import numpy as np
import matplotlib.pyplot as plt

rdx100 = np.random.randn(100)
rdy100 = np.random.randn(100)

rdcolors100 = np.random.randn(100)
rdsizes100 = np.abs(np.random.randn(100) * 1000)

plt.scatter(rdx100, rdy100, c=rdcolors100,
            s=rdsizes100, alpha=0.3, cmap='viridis')

plt.colorbar()

plt.show()
