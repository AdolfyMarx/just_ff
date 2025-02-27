import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5, 2 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()