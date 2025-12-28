import numpy as np

def manual_cross_product(a, b):
    c_x = (a[1]*b[2]) - (a[2]*b[1])
    c_y = (a[2]*b[0]) - (a[0]*b[2])
    c_z = (a[0]*b[1]) - (a[1]*b[0])
    return np.array([c_x, c_y, c_z])

vector_r = np.array([0.5, 0.0, 0.0])
vector_F = np.array([0.0, 0.0, -10.0])

torque = manual_cross_product(vector_r,vector_F)
print(f"Manual Torque is {torque}")

print(f"Cross product using numpy is {np.cross(vector_r, vector_F)}")

