import numpy as np
import matplotlib.pyplot as plt

array = np.array([4, 8, 15,16, 23, 42])
print(array)
print(array[::-1])

x_values = np.linspace(0, np.pi, 100)
y_values = 2 * np.cos(x_values)
plt.plot(x_values, y_values)
plt.xlabel('X Values')
plt.ylabel('$2*\cos(x)$')
plt.show()