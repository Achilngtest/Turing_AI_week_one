import matplotlib.pyplot as plt
import numpy as np

def o():
    random_numbers = np.random.randn(100)
    random_numbers = abs(random_numbers)
    random_numbers[random_numbers < 0] = 0
    random_numbers[random_numbers > 2] = 2
    scaled_numbers = random_numbers  * 500
    return scaled_numbers

plt.figure(figsize=(5, 5))
x = np.random.randn(1, 1, 100)
y = np.random.randn(1, 1, 100)
sizes = o()
colors = np.random.randint(10, 200, size=100)

plt.scatter(x, y, s=sizes, c=colors, alpha=0.3,cmap='viridis')

plt.colorbar()

plt.show()