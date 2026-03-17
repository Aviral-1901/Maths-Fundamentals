"""
Topic: Partial Derivatives & Sensitivity Analysis
Scenario: Analyzing the thermal gradient of a 2D heat-sink plate.

Math Concept: 
- Partial Derivative (df/dx): Measuring slope while holding other variables constant.
- Grid Processing: Using np.meshgrid and np.gradient to find vector fields.

Goal: 
Calculate the local slope in the X and Y directions at a specific point (2, 0).
This identifies how sensitive the temperature is to movement in either direction.

Verification:
For T(x,y) = x^2 + y^2, the analytical derivatives are:
- dT/dx = 2x  (Expected at x=2: 4.0)
- dT/dy = 2y  (Expected at y=0: 0.0)
"""
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
dx = x[1] - x[0]
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

grad_y, grad_x = np.gradient(Z, dx) #here spacing is  dx = 0.1 distance between two points

idx_x = np.argmin(np.abs(x - 2.0))
idx_y = np.argmin(np.abs(y - 0.0))

print(f"Slope in X direction: {grad_x[idx_y, idx_x]}")
print(f"Slope in Y direction: {grad_y[idx_y, idx_x]}")