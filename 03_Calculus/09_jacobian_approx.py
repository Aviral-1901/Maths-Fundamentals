import numpy as np

def f(state):
    eps = 1e-6
    r = state[0]
    theta = state[1]

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return np.array([x, y])

r = 2.0
theta = np.radians(45)
current_state = np.array([r, theta])

base_pos = f(current_state)

eps = 1e-6

state_r = np.array([r+eps, theta])
pos_r = f(state_r)
col1 = (pos_r - base_pos) / eps

state_theta = np.array([r, theta+eps])
pos_theta = f(state_theta)
col2 = (pos_theta - base_pos) / eps

j = np.column_stack((col1, col2))
print(j)