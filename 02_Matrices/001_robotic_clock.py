import numpy as np

theta = np.radians(30)
matrix = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta),np.cos(theta)]])
v = np.array([10.0, 0.0])

v_new = matrix @ v
print(v_new)