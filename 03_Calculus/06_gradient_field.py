import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

Z = np.exp(-(X**2 + Y**2))
dy, dx = np.gradient(Z)

u_escape = -dx
v_escape = -dy

plt.quiver(X, Y, u_escape, v_escape, color='red')
plt.contour(X, Y, Z)
plt.show()
