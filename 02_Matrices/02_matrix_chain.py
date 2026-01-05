# Demonstrating Non-Commutativity and Signal Distortion in Linear Transformations.
# Shows how an intermediate Shear transformation prevents a counter-rotation from canceling out the original noise.

import numpy as np

cam = np.array([10.0, 0.0])
theta = np.radians(10)

R_noise = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta), np.cos(theta)]])

R_correct = np.array([[np.cos(-theta), -np.sin(-theta)],
                     [np.sin(-theta), np.cos(-theta)]])

shear = np.array([[1, 0.5],[0, 1]])

path_A = R_correct @ R_noise @ cam
path_B = R_correct @ shear @ R_noise @ cam

print("the result in path A is",path_A)
print("The result in path B",path_B)