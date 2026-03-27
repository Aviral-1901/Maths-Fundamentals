import numpy as np

x = np.array([2.0, 3.0])
w = np.array([0.5, -1.0])

u = w @ x
y = u**2

dy_du = 2*u
du_dw = x
dy_dw = dy_du * du_dw

print(dy_dw)