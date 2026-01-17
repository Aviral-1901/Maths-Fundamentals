"""
Topic: Linear Systems & Inverses
Scenario: Decoupling interfering sensors (Temperature & Humidity).

Math Model: A * x = b
- A (Mixing Matrix): How the sensors cross-talk.
- x (Unknown Input): The True Temperature/Humidity.
- b (Measurement): The raw sensor readings.

Objective: Find x given A and b.
Method: Use np.linalg.solve() (Gaussian Elimination) instead of finding the full Inverse matrix.
"""

import numpy as np

A = np.array([[3, 1], [1, 2]])
b = np.array([25.0, 10.0])

x = np.linalg.solve(A, b)

print("the true value[input] was",x)
print("checking again :",A@x)
