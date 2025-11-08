import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.unicode_minus'] = False

np.random.seed(42)
x = np.random.randn(100)
y = np.random.randn(100)

colors_ = np.random.randn(100)
colors = (colors_ - colors_.min()) / (colors_.max() - colors_.min()) * 1000 + 0

sizes_ = np.random.randn(100)
sizes = (sizes_ - sizes_.min()) / (sizes_.max() - sizes_.min()) * 1000 + 0

scatter = plt.scatter(
    x, y,
    c=colors,
    s=sizes,
    alpha=0.3,
    cmap='viridis'
)

colorbar = plt.colorbar(scatter)
colorbar.set_ticks([200, 400, 600, 800])
colorbar.set_ticklabels(['0.2', '0.4', '0.6', '0.8'])

plt.show()