import numpy as np

def get_rotation_matrix(degrees):
    theta = np.radians(degrees)
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([[c,-s],[s,c]])

v = np.array([1,0]) #points east
v_new = get_rotation_matrix(90) @ v
print(np.round(v_new))
v_new2 = get_rotation_matrix(90) @ v_new
print(np.round(v_new2))